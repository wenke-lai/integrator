from pulumi_aws import iam

from diagrams.eraser import cloud_architecture as diagram


class User(iam.User):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new IAM User.

        Args:
            name (str): The name of the IAM User.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/iam/user/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name + "-user", icon="aws-iam-identity-center")
