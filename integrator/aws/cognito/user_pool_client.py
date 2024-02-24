from pulumi_aws import cognito

from diagrams.eraser import cloud_architecture as diagram


class UserPoolClient(cognito.UserPoolClient):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new Cognito User Pool Client.

        Args:
            name (str): The name of the Cognito User Pool Client.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cognito/userpoolclient/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name + "user-pool-client", icon="aws-cognito")
