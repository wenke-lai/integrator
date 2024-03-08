from pulumi_aws import cognito

from diagrams.eraser import cloud_architecture as diagram


class UserPool(cognito.UserPool):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new Cognito User Pool.

        Args:
            resource_name (str): The name of the Cognito User Pool.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cognito/userpool/#inputs)
        """

        super().__init__(resource_name, **kwargs)

        self.diagram = diagram.Node(resource_name + "user-pool", icon="aws-cognito")
