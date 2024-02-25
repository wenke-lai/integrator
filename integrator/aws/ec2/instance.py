from __future__ import annotations

import typing

from pulumi_aws import ec2

from diagrams.eraser import cloud_architecture as diagram

if typing.TYPE_CHECKING:
    from .launch_template import LaunchTemplate
    from .security_group import SecurityGroup
    from .subnet import Subnet


class Instance(ec2.Instance):
    def __init__(
        self,
        name: str,
        launch_template: LaunchTemplate,
        subnet: Subnet,
        security_group: SecurityGroup,
        **kwargs,
    ) -> None:
        """Create a new EC2 Instance.

        Args:
            name (str): The name of the EC2 Instance.
            launch_template (LaunchTemplate): The Launch Template to use for the instance.
            subnet (Subnet): The subnet to launch the instance in.
            security_group (SecurityGroup): The security group to attach to the instance.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/instance/#inputs)
        """
        super().__init__(
            name,
            subnet_id=subnet.id,
            vpc_security_group_ids=[security_group.id],
            launch_template={"id": launch_template.id},
            **kwargs,
        )
        self.diagram = diagram.Node(name, icon="aws-ec2")
