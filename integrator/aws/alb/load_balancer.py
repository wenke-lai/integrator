from __future__ import annotations

from typing import TYPE_CHECKING

from pulumi_aws import alb

from diagrams.eraser import cloud_architecture as diagram

from .listener import DefaultAction, Listener
from .target_group import TargetGroup

if TYPE_CHECKING:
    from ..ec2.security_group import SecurityGroup
    from ..ec2.subnet import Subnet


class LoadBalancer(alb.LoadBalancer):
    def __init__(
        self,
        resource_name: str,
        security_groups: list[SecurityGroup],
        subnets: list[Subnet],
        internal: bool = False,
        **kwargs,
    ) -> None:
        """Create a new LoadBalancer.

        Args:
            resource_name (str): The name of the LoadBalancer.
            security_groups (list): A list of security groups to associate with the LoadBalancer.
            subnets (list): A list of subnets to associate with the LoadBalancer.
            internal (bool, optional): If true, the LoadBalancer will be internal. Defaults to False.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/alb/loadbalancer/#inputs)
        """
        super().__init__(
            resource_name,
            load_balancer_type="application",
            security_groups=[sg.id for sg in security_groups],
            subnets=[subnet.id for subnet in subnets],
            internal=internal,
            **kwargs,
        )

        self.diagram = diagram.Group(resource_name, icon="aws-elastic-load-balancing")

    def create_target_group(
        self,
        resource_name: str,
        vpc_id: str,
        port: int = 443,
        protocol: str = "HTTPS",
        **kwargs,
    ) -> TargetGroup:
        target_group = TargetGroup(
            resource_name, port=port, protocol=protocol, vpc_id=vpc_id, **kwargs
        )
        self.diagram.append(target_group.diagram)
        return target_group

    def create_listener(
        self,
        resource_name: str,
        target_group: TargetGroup,
        certificate_arn: str,
        **kwargs,
    ):
        default_action = DefaultAction.create_forward(target_group_arn=target_group.arn)
        listener = Listener(
            resource_name,
            load_balancer_arn=self.arn,
            certificate_arn=certificate_arn,
            default_actions=[default_action],
            **kwargs,
        )

        self.diagram.append(listener.diagram)
        listener.diagram.edges.connect(target_group.diagram)
        return listener
