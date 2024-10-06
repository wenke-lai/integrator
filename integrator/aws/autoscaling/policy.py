from pulumi_aws import autoscaling


class Policy(autoscaling.Policy):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new AutoScaling Group.

        Args:
            resource_name (str): The name of the AutoScaling Group.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/autoscaling/group/#inputs)
        """
        super().__init__(resource_name, **kwargs)
