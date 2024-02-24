from pulumi_aws import ec2

from diagrams.eraser import cloud_architecture as diagram


class Instance(ec2.Instance):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new EC2 Instance.

        Args:
            name (str): The name of the EC2 Instance.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/instance/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name, icon="aws-ec2")
