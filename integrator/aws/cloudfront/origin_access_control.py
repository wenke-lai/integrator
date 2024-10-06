from pulumi_aws import cloudfront


class OriginAccessControl(cloudfront.OriginAccessControl):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new Origin Access Control.

        Args:
            resource_name (str): The name of the Origin Access Control.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cloudfront/originaccesscontrol/#inputs)
        """
        super().__init__(resource_name, **kwargs)


class S3OriginAccessControl(cloudfront.OriginAccessControl):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new S3 Origin Access Control.

        Args:
            resource_name (str): The name of the S3 Origin Access Control.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cloudfront/originaccesscontrol/#inputs)
        """

        super().__init__(
            resource_name,
            origin_access_control_origin_type="s3",
            signing_behavior="always",
            signing_protocol="sigv4",
            **kwargs,
        )
