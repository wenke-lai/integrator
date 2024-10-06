from pulumi_aws import scheduler


class Schedule(scheduler.Schedule):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new AWS Schedule.

        Args:
            resource_name (str): The name of the AWS Schedule.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/scheduler/schedule/#inputs)
        """

        super().__init__(resource_name, **kwargs)
