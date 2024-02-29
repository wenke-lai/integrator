from pulumi_aws import cloudwatch

from diagrams.eraser import cloud_architecture as diagram


class LogResourcePolicy(cloudwatch.LogResourcePolicy):

    def __init__(self, name: str, **kwargs) -> None:
        """Create a new Log Resource Policy.

        Args:
            name (str): The name of the Log Resource Policy.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cloudwatch/logresourcepolicy/#inputs)
        """

        kwargs.setdefault("policy_name", name)
        super().__init__(name, **kwargs)
        self.diagram = diagram.Group(name, icon="aws-cloudwatch")
