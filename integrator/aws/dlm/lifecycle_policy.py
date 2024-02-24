from pulumi_aws import dlm

from diagrams.eraser import cloud_architecture as diagram


class LifecyclePolicy(dlm.LifecyclePolicy):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new DLM Lifecycle Policy.

        Args:
            name (str): The name of the DLM Lifecycle Policy.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/dlm/lifecyclepolicy/#inputs)
        """
        super().__init__(name, **kwargs)

        self.diagram = diagram.Node(name + "-lifecycle-policy", icon="aws-ec2")
