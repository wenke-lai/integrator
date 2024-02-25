from pulumi_aws import kms

from diagrams.eraser import cloud_architecture as diagram


class Key(kms.Key):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new KMS Key.

        Args:
            name (str): The name of the KMS Key.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/kms/key/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name + "-key", icon="aws-kms")
