from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pulumi_aws import cloudfront, iam

from diagrams.eraser import cloud_architecture as diagram

from ..s3.bucket_policy import BucketPolicy

if TYPE_CHECKING:
    from ..acm import Certificate
    from ..s3 import Bucket
    from .cache_policy import CachePolicy
    from .origin_access_control import OriginAccessControl
    from .response_header_policy import ResponseHeaderPolicy


class Distribution(cloudfront.Distribution):
    def __init__(
        self,
        name: str,
        domain_name: str,
        bucket: Bucket,
        origin_access_control: OriginAccessControl,
        cache_policy: CachePolicy,
        ordered_cache_policy: CachePolicy,
        response_header_policy: ResponseHeaderPolicy,
        certificate: Optional[Certificate] = None,
        http_version: str = "http1.1",
        enabled: bool = True,
        **kwargs,
    ) -> None:
        """Create a new CloudFront Distribution.

        Args:
            name (str): The name of the CloudFront Distribution.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cloudfront/distribution/#inputs)
        """
        kwargs.setdefault("comment", domain_name)

        aliases = None
        viewer_certificate = cloudfront.DistributionViewerCertificateArgs(
            cloudfront_default_certificate=True,
            ssl_support_method="sni-only",
            minimum_protocol_version="TLSv1.2_2021",
        )
        if certificate:
            aliases = [domain_name]
            viewer_certificate = cloudfront.DistributionViewerCertificateArgs(
                acm_certificate_arn=certificate.arn,
                ssl_support_method="sni-only",
                minimum_protocol_version="TLSv1.2_2021",
            )

        super().__init__(
            name,
            enabled=enabled,
            http_version=http_version,
            is_ipv6_enabled=True,
            # CNAME & SSL
            aliases=aliases,
            viewer_certificate=viewer_certificate,
            price_class="PriceClass_100",
            default_root_object="index.html",
            # Origin
            origins=[
                cloudfront.DistributionOriginArgs(
                    domain_name=bucket.bucket_regional_domain_name,
                    origin_id=bucket.id,
                    origin_access_control_id=origin_access_control.id,
                )
            ],
            # Behavior
            default_cache_behavior=cloudfront.DistributionDefaultCacheBehaviorArgs(
                allowed_methods=["GET", "HEAD"],
                cached_methods=["GET", "HEAD"],
                viewer_protocol_policy="redirect-to-https",
                compress=True,
                target_origin_id=bucket.id,
                cache_policy_id=cache_policy.id,  # default (main) cache policy
                response_headers_policy_id=response_header_policy.id,
            ),
            ordered_cache_behaviors=[
                cloudfront.DistributionOrderedCacheBehaviorArgs(
                    path_pattern="/index.html",
                    allowed_methods=["GET", "HEAD"],
                    cached_methods=["GET", "HEAD"],
                    viewer_protocol_policy="redirect-to-https",
                    compress=True,
                    target_origin_id=bucket.id,
                    cache_policy_id=ordered_cache_policy.id,  # ordered cache policy
                    response_headers_policy_id=response_header_policy.id,
                ),
            ],
            # Error (for SPA)
            custom_error_responses=[
                cloudfront.DistributionCustomErrorResponseArgs(
                    error_code=404,
                    response_code=200,
                    response_page_path="/index.html",
                    error_caching_min_ttl=300,
                ),
                cloudfront.DistributionCustomErrorResponseArgs(
                    error_code=403,
                    response_code=200,
                    response_page_path="/index.html",
                    error_caching_min_ttl=300,
                ),
            ],
            # GEO
            restrictions=cloudfront.DistributionRestrictionsArgs(
                geo_restriction=cloudfront.DistributionRestrictionsGeoRestrictionArgs(
                    restriction_type="none",
                )
            ),
            # Logger
            # logging_config=aws.cloudfront.DistributionLoggingConfigArgs(
            #     bucket=log_bucket.id,
            #     include_cookies=True,
            # ),
            **kwargs,
        )

        self.diagram = diagram.Node(name, icon="aws-cloudfront")

        document = iam.get_policy_document(
            version="2008-10-17",
            policy_id="PolicyForCloudFrontPrivateContent",
            statements=[
                iam.GetPolicyDocumentStatementArgs(
                    sid="AllowCloudFrontServicePrincipal",
                    effect="Allow",
                    principals=[
                        iam.GetPolicyDocumentStatementPrincipalArgs(
                            type="Service",
                            identifiers=["cloudfront.amazonaws.com"],
                        )
                    ],
                    actions=["s3:GetObject"],
                    resources=[bucket.arn.apply(lambda arn: arn + "/*")],
                    conditions=[
                        iam.GetPolicyDocumentStatementConditionArgs(
                            test="StringEquals",
                            variable="AWS:SourceArn",
                            values=[self.arn],
                        )
                    ],
                )
            ],
        )
        BucketPolicy(name, bucket=bucket, policy=document.json)
