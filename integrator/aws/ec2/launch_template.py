from pulumi_aws import ec2

from diagrams.eraser import cloud_architecture as diagram

from .instance import Instance


class LaunchTemplate(ec2.LaunchTemplate):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new EC2 Launch Template.

        Args:
            name (str): The name of the EC2 Launch Template.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/launchtemplate/#inputs)
        """
        super().__init__(name, **kwargs)

        self.diagram = diagram.Node(name, icon="aws-ec2")

    def create_instance(self, name: str, **kwargs) -> ec2.Instance:
        """Create a new EC2 Instance using this Launch Template.

        Args:
            name (str): The name of the EC2 Instance.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/instance/#inputs)

        Returns:
            ec2.Instance: The new EC2 Instance.
        """
        instance = Instance(name, launch_template=self, **kwargs)
        self.diagram.edges.connect(instance.diagram)
        return instance
