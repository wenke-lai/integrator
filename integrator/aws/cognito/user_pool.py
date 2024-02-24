from pulumi_aws import cognito

from diagrams.eraser import cloud_architecture as diagram


class UserPool(cognito.UserPool):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new Cognito User Pool.

        Args:
            name (str): The name of the Cognito User Pool.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cognito/userpool/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name + "user-pool", icon="aws-cognito")
