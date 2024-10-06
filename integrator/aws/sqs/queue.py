from pulumi_aws import sqs


class Queue(sqs.Queue):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new SQS Queue.

        Args:
            resource_name (str): The name of the SQS Queue.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/sqs/queue/#inputs)
        """

        super().__init__(resource_name, **kwargs)
