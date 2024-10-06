from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from pulumi_aws import autoscaling

if TYPE_CHECKING:
    from ..ec2.launch_template import LaunchTemplate
    from ..ec2.subnet import Subnet


class Group(autoscaling.Group):
    def __init__(
        self,
        resource_name: str,
        launch_template: LaunchTemplate,
        min_size: int,
        max_size: int,
        subnets: list[Subnet],
        health_check_type: Literal["EC2", "ELB"] = "ELB",
        health_check_grace_period: int = 300,
        **kwargs,
    ) -> None:
        """Create a new AutoScaling Group.

        Args:
            resource_name (str): The name of the AutoScaling Group.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/autoscaling/group/#inputs)
        """
        super().__init__(
            resource_name,
            min_size=min_size,
            max_size=max_size,
            launch_template=autoscaling.GroupLaunchTemplateArgs(
                id=launch_template.id,
                version="$Latest",
            ),
            vpc_zone_identifiers=[subnet.id for subnet in subnets],
            health_check_type=health_check_type,
            health_check_grace_period=health_check_grace_period,
            **kwargs,
        )
