from pulumi_aws import cognito

from diagrams.eraser import cloud_architecture as diagram


class UserPoolDomain(cognito.UserPoolDomain):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new Cognito User Pool Domain.

        Args:
            name (str): The name of the Cognito User Pool Domain.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cognito/userpooldomain/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name + "user-pool-domain", icon="aws-cognito")
