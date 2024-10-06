from __future__ import annotations

import typing

import pulumi
from pulumi_aws import ec2


if typing.TYPE_CHECKING:
    from .launch_template import LaunchTemplate
    from .security_group import SecurityGroup
    from .subnet import Subnet


class Instance(ec2.Instance):
    def __init__(
        self,
        resource_name: str,
        launch_template: LaunchTemplate,
        subnet: Subnet,
        security_group: SecurityGroup,
        **kwargs,
    ) -> None:
        """Create a new EC2 Instance.

        Args:
            resource_name (str): The name of the EC2 Instance.
            launch_template (LaunchTemplate): The Launch Template to use for the instance.
            subnet (Subnet): The subnet to launch the instance in.
            security_group (SecurityGroup): The security group to attach to the instance.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/instance/#inputs)
        """
        kwargs.setdefault("tags", {"Name": resource_name})
        kwargs.setdefault(
            "opts", pulumi.ResourceOptions(ignore_changes=["tags", "default_tags"])
        )
        super().__init__(
            resource_name,
            subnet_id=subnet.id,
            vpc_security_group_ids=[security_group.id],
            launch_template={"id": launch_template.id},
            **kwargs,
        )
