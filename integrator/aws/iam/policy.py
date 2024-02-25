from pulumi_aws import iam

from diagrams.eraser import cloud_architecture as diagram


class Policy(iam.Policy):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new IAM Policy.

        Args:
            name (str): The name of the IAM Policy.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/iam/policy/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name + "-policy", icon="aws-iam-identity-center")
