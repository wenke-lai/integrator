from pulumi_aws import scheduler

from diagrams.eraser import cloud_architecture as diagram


class ScheduleGroup(scheduler.ScheduleGroup):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new AWS Schedule Group.

        Args:
            name (str): The name of the AWS Schedule Group.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/scheduler/schedulegroup/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Group(name + "-schedule-group", icon="aws-eventbridge")
