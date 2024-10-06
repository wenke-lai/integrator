from pulumi_aws import scheduler


class ScheduleGroup(scheduler.ScheduleGroup):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new AWS Schedule Group.

        Args:
            resource_name (str): The name of the AWS Schedule Group.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/scheduler/schedulegroup/#inputs)
        """

        super().__init__(resource_name, **kwargs)
