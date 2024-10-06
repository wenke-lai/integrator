from pulumi_aws import cloudfront


class ResponseHeaderPolicy(cloudfront.ResponseHeadersPolicy):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new Response Header Policy.

        Args:
            resource_name (str): The name of the Response Header Policy.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cloudfront/responseheaderpolicy/#inputs)
        """

        super().__init__(resource_name, **kwargs)
