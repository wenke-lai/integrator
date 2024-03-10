from typing import Optional

from pulumi_aws import ec2, get_availability_zones

from diagrams.eraser import cloud_architecture as diagram

from .internet_gateway import GatewayRoute, InternetGateway
from .security_group import SecurityGroup
from .subnet import PrivateSubnet, PublicSubnet


class Vpc(ec2.Vpc):
    def __init__(
        self,
        resource_name: str,
        cidr_block: Optional[str] = "10.0.0.0/16",
        enable_dns_hostnames: Optional[bool] = True,
        **kwargs,
    ) -> None:
        """Create a new VPC.

        Args:
            resource_name (str): The name of the VPC.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/vpc/#inputs)
        """
        kwargs.setdefault("tags", {"Name": resource_name})
        super().__init__(
            resource_name,
            cidr_block=cidr_block,
            enable_dns_hostnames=enable_dns_hostnames,
            **kwargs,
        )
        self.diagram = diagram.Group(resource_name, icon="aws-ec2")

        self.availability_zones: list[str] = self.get_availability_zones()

    def get_availability_zones(self, max_azs: Optional[int] = None) -> list[str]:
        available = get_availability_zones(state="available")
        if max_azs:
            return available.names[:max_azs]
        return available.names  # full list of available AZs

    def set_availability_zones(self, max_azs: Optional[int] = None) -> None:
        self.availability_zones = self.get_availability_zones(max_azs)

    def create_internet_gateway(self, resource_name: str) -> None:
        """Create a new internet gateway and attach it to the VPC.

        Args:
            name (str): The name of the internet gateway.
        """
        internet_gateway = InternetGateway(resource_name, vpc=self)
        default_route = GatewayRoute(resource_name, vpc=self, gateway=internet_gateway)
        return internet_gateway, default_route

    def create_public_subnet(
        self, resource_name: str, availability_zone: str, cidr_block: str, **kwargs
    ) -> PublicSubnet:
        """Create a new public subnet in the VPC.
        Args:
            resource_name (str): The name of the subnet.
            availability_zone (str): The availability zone for the subnet.
            cidr_block (str): The CIDR block for the subnet.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/subnet/#inputs)

        Returns:
            PublicSubnet: The created public subnet.
        """
        return PublicSubnet(
            resource_name,
            availability_zone=availability_zone,
            cidr_block=cidr_block,
            vpc=self,
            **kwargs,
        )

    def create_private_subnet(
        self, resource_name: str, availability_zone: str, cidr_block: str, **kwargs
    ) -> PrivateSubnet:
        """Create a new Private subnet in the VPC.
        Args:
            resource_name (str): The name of the subnet.
            availability_zone (str): The availability zone for the subnet.
            cidr_block (str): The CIDR block for the subnet.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/subnet/#inputs)

        Returns:
            PrivateSubnet: The created private subnet.
        """
        return PrivateSubnet(
            resource_name,
            availability_zone=availability_zone,
            cidr_block=cidr_block,
            vpc=self,
            **kwargs,
        )

    def create_security_group(self, resource_name: str, **kwargs) -> SecurityGroup:
        """Create a new security group to the VPC.

        Args:
            name (str): The name of the security group.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/securitygroup/#inputs)

        Returns:
            ec2.SecurityGroup: The created security group.
        """
        return SecurityGroup(resource_name, vpc=self, **kwargs)
