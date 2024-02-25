from __future__ import annotations

from typing import TYPE_CHECKING

import pulumi
from pulumi_aws import ec2

from diagrams.eraser import cloud_architecture as diagram

if TYPE_CHECKING:
    from .vpc import Vpc


class InternetGateway(ec2.InternetGateway):
    def __init__(self, name: str, vpc: Vpc, **kwargs) -> None:
        """Create a new internet gateway.

        Args:
            name (str): The name of the internet gateway.
            vpc (Vpc): The VPC to attach the internet gateway to.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/internetgateway/#inputs)
        """
        super().__init__(
            name, vpc_id=vpc.id, opts=pulumi.ResourceOptions(parent=vpc), **kwargs
        )
        self.diagram = diagram.Node(name)


class GatewayRoute(ec2.Route):
    def __init__(self, name: str, vpc: Vpc, gateway: InternetGateway) -> None:
        """Create a new default route between the VPC and the internet gateway.

        Args:
            name (str): The name of the route.
            vpc (Vpc): The VPC to add the route to.
            gateway (InternetGateway): The internet gateway to route traffic to.
        """
        super().__init__(
            f"{name}-default-route",
            route_table_id=vpc.default_route_table_id,
            gateway_id=gateway.id,
            opts=pulumi.ResourceOptions(parent=gateway),
        )
        gateway.diagram.edges.connect(vpc.diagram)
