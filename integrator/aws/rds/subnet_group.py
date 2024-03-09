from __future__ import annotations

from typing import TYPE_CHECKING

from pulumi_aws import rds

if TYPE_CHECKING:
    from ..ec2.subnet import Subnet


class SubnetGroup(rds.SubnetGroup):
    def __init__(self, resource_name: str, subnets: list[Subnet], **kwargs) -> None:
        """Create a new RDS Subnet Group.

        Args:
            resource_name (str): The name of the RDS Subnet Group.
            subnets (list[Subnet]): A list of Subnet objects.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/rds/subnetgroup/#inputs)
        """

        super().__init__(
            resource_name, subnet_ids=[subnet.id for subnet in subnets], **kwargs
        )
