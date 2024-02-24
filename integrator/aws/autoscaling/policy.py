from pulumi_aws import autoscaling

from diagrams.eraser import cloud_architecture as diagram


class Policy(autoscaling.Policy):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new AutoScaling Group.

        Args:
            name (str): The name of the AutoScaling Group.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/autoscaling/group/#inputs)
        """
        super().__init__(name, **kwargs)

        self.diagram = diagram.Node(name + "policy", icon="aws-ec2-auto-scaling")
