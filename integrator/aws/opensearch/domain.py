from __future__ import annotations

from typing import TYPE_CHECKING

from pulumi_aws import iam, opensearch

from diagrams.eraser import cloud_architecture as diagram

from ..cloudwatch import LogGroup, LogResourcePolicy

if TYPE_CHECKING:
    from ..acm import Certificate
    from ..ec2.security_group import SecurityGroup
    from ..ec2.subnet import Subnet


class Domain(opensearch.Domain):

    def __init__(
        self,
        name: str,
        subnets: list[Subnet],
        security_group: SecurityGroup,
        instance_count: int = 1,
        instance_type: str = "t3.medium.search",
        volume_size: int = 10,
        # todo: implement master props
        # master_count: int = 0,
        # master_type: str = "t3.medium.search",
        endpoint: str = None,
        certificate: Certificate = None,
        **kwargs,
    ) -> None:
        """Create a new OpenSearch Domain.

        Args:
            name (str): The name of the OpenSearch Domain.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/opensearch/domain/#inputs)
        """

        if len(subnets) < instance_count:
            raise ValueError(
                "subnets should be equal to or greater than instance count."
            )
        subnet_ids = [subnet.id for subnet in subnets[:instance_count]]

        cluster_config = opensearch.DomainClusterConfigArgs(
            instance_count=instance_count,
            instance_type=instance_type,
            zone_awareness_enabled=True,
            zone_awareness_config=opensearch.DomainClusterConfigZoneAwarenessConfigArgs(
                availability_zone_count=3,
            ),
        )
        if instance_count == 1:
            # single node
            cluster_config.zone_awareness_enabled = False
            cluster_config.zone_awareness_config = None

        domain_endpoint_options = None
        if endpoint & certificate:
            domain_endpoint_options = opensearch.DomainDomainEndpointOptionsArgs(
                enforce_https=True,
                custom_endpoint_enabled=True,
                custom_endpoint=endpoint,
                custom_endpoint_certificate_arn=certificate.arn,
                tls_security_policy="Policy-Min-TLS-1-0-2019-07",
            )

        index_slow_logs = LogGroup(name=f"{name}-index-slow-logs")
        search_slow_logs = LogGroup(name=f"{name}-search-slow-logs")
        es_application_logs = LogGroup(name=f"{name}-es-application-logs")
        audit_logs = LogGroup(name=f"{name}-audit-logs")
        document = iam.get_policy_document(
            statements=[
                iam.GetPolicyDocumentStatementArgs(
                    effect="Allow",
                    principals=[
                        iam.GetPolicyDocumentStatementPrincipalArgs(
                            type="Service", identifiers=["es.amazonaws.com"]
                        )
                    ],
                    actions=[
                        "logs:CreateLogStream",
                        "logs:PutLogEvents",
                        "logs:PutLogEventsBatch",
                    ],
                    resources=[
                        index_slow_logs.arn.apply(lambda arn: f"{arn}:*"),
                        search_slow_logs.arn.apply(lambda arn: f"{arn}:*"),
                        es_application_logs.arn.apply(lambda arn: f"{arn}:*"),
                        audit_logs.arn.apply(lambda arn: f"{arn}:*"),
                    ],
                )
            ]
        )
        LogResourcePolicy(name, policy_name=name, policy_document=document.json)

        super().__init__(
            name,
            domain_name=name,
            engine_version="OpenSearch_2.11",
            # Node
            cluster_config=cluster_config,
            ebs_options=opensearch.DomainEbsOptionsArgs(
                ebs_enabled=True,
                volume_size=volume_size,
                volume_type="gp3",
            ),
            # Network
            vpc_options=opensearch.DomainVpcOptionsArgs(
                security_group_ids=[security_group.id],
                subnet_ids=subnet_ids,
            ),
            encrypt_at_rest=opensearch.DomainEncryptAtRestArgs(
                # Configuration block for encrypt at rest options
                enabled=False,
            ),
            node_to_node_encryption=opensearch.DomainNodeToNodeEncryptionArgs(
                enabled=True,
            ),
            domain_endpoint_options=domain_endpoint_options,
            # Log
            log_publishing_options=[
                opensearch.DomainLogPublishingOptionArgs(
                    cloudwatch_log_group_arn=index_slow_logs.arn.apply(
                        lambda arn: f"{arn}:*"
                    ),
                    log_type="INDEX_SLOW_LOGS",
                ),
                opensearch.DomainLogPublishingOptionArgs(
                    cloudwatch_log_group_arn=search_slow_logs.arn.apply(
                        lambda arn: f"{arn}:*"
                    ),
                    log_type="SEARCH_SLOW_LOGS",
                ),
                opensearch.DomainLogPublishingOptionArgs(
                    cloudwatch_log_group_arn=es_application_logs.arn.apply(
                        lambda arn: f"{arn}:*"
                    ),
                    log_type="ES_APPLICATION_LOGS",
                ),
                opensearch.DomainLogPublishingOptionArgs(
                    cloudwatch_log_group_arn=audit_logs.arn.apply(
                        lambda arn: f"{arn}:*"
                    ),
                    log_type="AUDIT_LOGS",
                    # audit log publishing cannot be enabled
                    # as you do not have advanced security options configured.
                    enabled=False,
                ),
            ],
            **kwargs,
        )
        self.diagram = diagram.Node(name, icon="aws-opensearch-service")
