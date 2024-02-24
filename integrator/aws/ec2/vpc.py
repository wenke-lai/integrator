from pulumi_aws import ec2

from diagrams.eraser import cloud_architecture as diagram

# from .security_group import SecurityGroup
# from .subnet import Subnet


class Vpc(ec2.Vpc):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new VPC.

        Args:
            name (str): The name of the VPC.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/vpc/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Group(name, icon="aws-ec2")

    def add_gateway(self, name: str, **kwargs) -> ec2.InternetGateway:
        """Add a new internet gateway to the VPC.

        Args:
            name (str): The name of the internet gateway.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/internetgateway/#inputs)

        Returns:
            ec2.InternetGateway: The created internet gateway.
        """

    def add_subnet(self, name: str, **kwargs) -> ec2.Subnet:
        """Add a new subnet to the VPC.

        Args:
            name (str): The name of the subnet.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/subnet/#inputs)

        Returns:
            ec2.Subnet: The created subnet.
        """

    def add_security_group(self, name: str, **kwargs) -> ec2.SecurityGroup:
        """Add a new security group to the VPC.

        Args:
            name (str): The name of the security group.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/securitygroup/#inputs)

        Returns:
            ec2.SecurityGroup: The created security group.
        """
