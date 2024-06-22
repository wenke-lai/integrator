from datetime import datetime, timezone

from pulumi_aws import apigateway


class Stage(apigateway.Stage):
    def __init__(
        self,
        resource_name: str,
        stage_name: str,
        rest_api: str,
        deployment: str = "",
        **kwargs,
    ) -> None:
        """Create a new API Gateway Stage.

        Args:
            resource_name (str): The name of the API Gateway Stage.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/apigateway/stage/#inputs)
        """
        if deployment == "":
            deployment = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

        super().__init__(
            resource_name,
            stage_name=stage_name,
            rest_api=rest_api,
            deployment=deployment,
            **kwargs,
        )
