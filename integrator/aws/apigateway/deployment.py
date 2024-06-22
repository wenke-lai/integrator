from pulumi_aws import apigateway


class Deployment(apigateway.Deployment):
    def __init__(self, resource_name: str, rest_api: str, **kwargs) -> None:
        """Create a new API Gateway Deployment."""

        super().__init__(resource_name, rest_api=rest_api, **kwargs)
