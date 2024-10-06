from pulumi_aws import cloudwatch


class LogResourcePolicy(cloudwatch.LogResourcePolicy):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new Log Resource Policy.

        Args:
            resource_name (str): The name of the Log Resource Policy.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cloudwatch/logresourcepolicy/#inputs)
        """

        kwargs.setdefault("policy_name", resource_name)

        super().__init__(resource_name, **kwargs)
