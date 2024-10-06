from __future__ import annotations

from typing import TYPE_CHECKING

import pulumi
from pulumi_aws import ec2

if TYPE_CHECKING:
    from .vpc import Vpc


class InternetGateway(ec2.InternetGateway):
    def __init__(self, resource_name: str, vpc: Vpc, **kwargs) -> None:
        """Create a new internet gateway.

        Args:
            resource_name (str): The name of the internet gateway.
            vpc (Vpc): The VPC to attach the internet gateway to.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/internetgateway/#inputs)
        """

        super().__init__(
            resource_name,
            vpc_id=vpc.id,
            opts=pulumi.ResourceOptions(parent=vpc),
            **kwargs,
        )


class GatewayRoute(ec2.Route):
    def __init__(self, resource_name: str, vpc: Vpc, gateway: InternetGateway) -> None:
        """Create a new default route between the VPC and the internet gateway.

        Args:
            resource_name (str): The name of the route.
            vpc (Vpc): The VPC to add the route to.
            gateway (InternetGateway): The internet gateway to route traffic to.
        """

        super().__init__(
            resource_name,
            route_table_id=vpc.default_route_table_id,
            gateway_id=gateway.id,
            destination_cidr_block="0.0.0.0/0",
            opts=pulumi.ResourceOptions(parent=gateway),
        )
