from pulumi_aws import sns

from diagrams.eraser import cloud_architecture as diagram


class Topic(sns.Topic):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new SNS Topic.

        Args:
            name (str): The name of the SNS Topic.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/sns/topic/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name, icon="aws-simple-notification-service")
