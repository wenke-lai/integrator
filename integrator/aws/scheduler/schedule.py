from pulumi_aws import scheduler

from diagrams.eraser import cloud_architecture as diagram


class Schedule(scheduler.Schedule):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new AWS Schedule.

        Args:
            name (str): The name of the AWS Schedule.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/scheduler/schedule/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name + "-schedule", icon="aws-eventbridge")
