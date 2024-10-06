from __future__ import annotations

import typing

from pulumi_aws import ec2

if typing.TYPE_CHECKING:
    from .vpc import Vpc


class Subnet(ec2.Subnet):
    def __init__(
        self,
        resource_name: str,
        availability_zone: str,
        cidr_block: str,
        vpc: Vpc,
        map_public_ip_on_launch: bool,
        **kwargs,
    ) -> None:
        """Create a new EC2 Subnet.

        Args:
            resource_name (str): The name of the EC2 Subnet.
            availability_zone (str): The availability zone for the subnet.
            cidr_block (str): The CIDR block for the subnet.
            vpc (Vpc): The VPC to create the subnet in.
            map_public_ip_on_launch (bool): Whether to map public IP on launch.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/subnet/#inputs)
        """
        kwargs.setdefault("tags", {"Name": resource_name})
        super().__init__(
            resource_name,
            availability_zone=availability_zone,
            cidr_block=cidr_block,
            vpc_id=vpc.id,
            map_public_ip_on_launch=map_public_ip_on_launch,
            **kwargs,
        )


class PublicSubnet(Subnet):
    def __init__(
        self,
        resource_name: str,
        availability_zone: str,
        cidr_block: str,
        vpc: Vpc,
        **kwargs,
    ) -> None:
        """Create a new public EC2 Subnet.

        Args:
            resource_name (str): The name of the public EC2 Subnet.
            availability_zone (str): The availability zone for the subnet.
            cidr_block (str): The CIDR block for the subnet.
            vpc (Vpc): The VPC to create the subnet in.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/subnet/#inputs)
        """
        super().__init__(
            resource_name,
            availability_zone=availability_zone,
            cidr_block=cidr_block,
            vpc=vpc,
            map_public_ip_on_launch=True,
            **kwargs,
        )


class PrivateSubnet(Subnet):
    def __init__(
        self,
        resource_name: str,
        availability_zone: str,
        cidr_block: str,
        vpc: Vpc,
        **kwargs,
    ) -> None:
        """Create a new private EC2 Subnet.

        Args:
            resource_name (str): The name of the private EC2 Subnet.
            availability_zone (str): The availability zone for the subnet.
            cidr_block (str): The CIDR block for the subnet.
            vpc (Vpc): The VPC to create the subnet in.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/subnet/#inputs)
        """
        super().__init__(
            resource_name,
            availability_zone=availability_zone,
            cidr_block=cidr_block,
            vpc=vpc,
            map_public_ip_on_launch=False,
            **kwargs,
        )
