from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import pulumi
from pulumi_aws import ec2

from diagrams.eraser import cloud_architecture as diagram

if TYPE_CHECKING:
    from .vpc import Vpc


class SecurityGroup(ec2.SecurityGroup):
    def __init__(self, resource_name: str, vpc: Vpc, **kwargs) -> None:
        """Create a new EC2 Security Group.

        Args:
            resource_name (str): The name of the EC2 Security Group.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/securitygroup/#inputs)
        """
        kwargs.setdefault("tags", {"Name": resource_name})
        super().__init__(resource_name, vpc_id=vpc.id, **kwargs)
        self.diagram = diagram.Node(resource_name, icon="aws-ec2")

        self.add_egress_rule(
            resource_name + "-default-outbound",
            port=0,
            protocol="-1",
            cidr_blocks=["0.0.0.0/0"],
        )

    def add_ingress_rule(
        self,
        resource_name: str,
        port: int,
        protocol: str,
        cidr_blocks: Optional[list[str]] = None,
        source_security_group_id: Optional[str] = None,
    ) -> ec2.SecurityGroupRule:
        """Add an ingress rule to the Security Group.

        Args:
            rule (ec2.SecurityGroupRule): The rule to add.
        """
        if cidr_blocks is None and source_security_group_id is None:
            raise ValueError(
                "Either `cidr_blocks` or `source_security_group_id` must be provided."
            )

        return ec2.SecurityGroupRule(
            resource_name,
            description=resource_name,
            security_group_id=self.id,
            type="ingress",
            from_port=port,
            to_port=port,
            protocol=protocol,
            cidr_blocks=cidr_blocks,
            source_security_group_id=source_security_group_id,
            opts=pulumi.ResourceOptions(parent=self),
        )

    def add_egress_rule(
        self,
        resource_name: str,
        port: int,
        protocol: str,
        cidr_blocks: Optional[list[str]] = None,
        source_security_group_id: Optional[str] = None,
    ) -> None:
        """Add an egress rule to the Security Group.

        Args:
            rule (ec2.SecurityGroupRule): The rule to add.
        """
        if cidr_blocks is None and source_security_group_id is None:
            raise ValueError(
                "Either `cidr_blocks` or `source_security_group_id` must be provided."
            )

        return ec2.SecurityGroupRule(
            resource_name,
            description=resource_name,
            security_group_id=self.id,
            type="egress",
            from_port=port,
            to_port=port,
            protocol=protocol,
            cidr_blocks=cidr_blocks,
            source_security_group_id=source_security_group_id,
            opts=pulumi.ResourceOptions(parent=self),
        )
