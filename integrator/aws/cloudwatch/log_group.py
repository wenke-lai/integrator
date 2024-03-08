from pulumi_aws import cloudwatch

from diagrams.eraser import cloud_architecture as diagram


class LogGroup(cloudwatch.LogGroup):
    def __init__(
        self, resource_name: str, retention_in_days: int = 30, **kwargs
    ) -> None:
        """Create a new Cloudwatch Log Group.

        Args:
            resource_name (str): The name of the log group.
            retention_in_days (int, optional): The number of days log events are kept in CloudWatch Logs. Defaults to 30.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cloudwatch/loggroup/#inputs)
        """

        super().__init__(resource_name, retention_in_days=retention_in_days, **kwargs)
        self.diagram = diagram.Node(resource_name, icon="aws-cloudwatch")
