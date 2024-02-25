from pulumi_aws import iam

from diagrams.eraser import cloud_architecture as diagram


class Role(iam.Role):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new IAM Role.

        Args:
            name (str): The name of the IAM Role.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/iam/role/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name + "-role", icon="aws-iam-identity-center")
