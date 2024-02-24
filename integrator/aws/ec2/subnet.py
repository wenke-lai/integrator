from pulumi_aws import ec2

from diagrams.eraser import cloud_architecture as diagram


class Subnet(ec2.Subnet):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new EC2 Subnet.

        Args:
            name (str): The name of the EC2 Subnet.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/subnet/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Group(name, icon="aws-ec2")
