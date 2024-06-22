import pulumi
from pulumi_aws import apigateway

from .deployment import Deployment
from .stage import Stage


class RestApi(apigateway.RestApi):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new API Gateway Rest API.

        Args:
            resource_name (str): The name of the API Gateway Rest API.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/apigateway/restapi/#inputs)
        """

        super().__init__(resource_name, **kwargs)

    def create_stage(self, resource_name: str, stage_name: str, **kwargs):
        """Create a new API Gateway Stage.

        Args:
            resource_name (str): The name of the API Gateway Stage.
            stage_name (str): The name of the stage.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/apigateway/stage/#inputs)
        """
        deployment = Deployment(
            resource_name,
            rest_api=self.id,
            opts=pulumi.ResourceOptions(delete_before_replace=True),
        )
        return Stage(
            resource_name,
            stage_name=stage_name,
            rest_api=self.id,
            deployment=deployment.id,
            **kwargs,
        )
