from pulumi_aws import autoscaling

from diagrams.eraser import cloud_architecture as diagram


class Group(autoscaling.Group):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new AutoScaling Group.

        Args:
            resource_name (str): The name of the AutoScaling Group.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/autoscaling/group/#inputs)
        """
        super().__init__(resource_name, **kwargs)

        self.diagram = diagram.Group(resource_name, icon="aws-ec2-auto-scaling")
