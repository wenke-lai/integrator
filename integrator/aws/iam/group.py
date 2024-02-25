from pulumi_aws import iam

from diagrams.eraser import cloud_architecture as diagram


class Group(iam.Group):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new IAM Group.

        Args:
            name (str): The name of the IAM Group.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/iam/group/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name + "-group", icon="aws-iam-identity-center")
