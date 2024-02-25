from pulumi_aws import sqs

from diagrams.eraser import cloud_architecture as diagram


class Queue(sqs.Queue):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new SQS Queue.

        Args:
            name (str): The name of the SQS Queue.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/sqs/queue/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name, icon="aws-simple-queue-service")
