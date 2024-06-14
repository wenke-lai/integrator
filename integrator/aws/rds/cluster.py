from __future__ import annotations

from typing import TYPE_CHECKING

from diagrams.eraser import cloud_architecture as diagram
from pulumi_aws import rds

from .cluster_instance import ServerlessV2Instance

if TYPE_CHECKING:
    from ..ec2.security_group import SecurityGroup
    from .subnet_group import SubnetGroup


class Cluster(rds.Cluster):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new RDS Cluster.

        Args:
            resource_name (str): The name of the RDS Cluster.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/rds/cluster/#inputs)
        """

        super().__init__(resource_name, **kwargs)

        self.diagram = diagram.Node(resource_name, icon="aws-rds")


class AuroraMySQLServerlessV2(Cluster):
    def __init__(
        self,
        resource_name: str,
        availability_zones: list[str],
        subnet_group: SubnetGroup,
        security_group: SecurityGroup,
        min_capacity: float = 0.5,
        max_capacity: float = 1,
        engine_version: str = "8.0.mysql_aurora.3.04.1",
        **kwargs,
    ) -> None:
        """Create a new Aurora MySQL Serverless v2 Cluster.

        Args:
            resource_name (str): The name of the RDS Cluster.
            availability_zones (list[str]): A list of Availability Zones.
            subnet_group (SubnetGroup): A SubnetGroup object.
            security_group (SecurityGroup): A SecurityGroup object.
            min_capacity (float, optional): The minimum capacity of the Aurora Serverless DB cluster. Defaults to 0.5.
            max_capacity (float, optional): The maximum capacity of the Aurora Serverless DB cluster. Defaults to 1.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/rds/cluster/#inputs)
        """

        super().__init__(
            resource_name,
            # Engine Options
            engine="aurora-mysql",
            engine_version=engine_version,
            # Settings
            master_username="admin",
            manage_master_user_password=True,
            # Instance configuration
            engine_mode="provisioned",  # provisioned == v2, serverless == v1
            serverlessv2_scaling_configuration=rds.ClusterServerlessv2ScalingConfigurationArgs(
                min_capacity=min_capacity,
                max_capacity=max_capacity,
            ),
            # Availability & durability
            availability_zones=availability_zones,
            # Connectivity
            network_type="IPV4",  # IPV4 | DUAL
            db_subnet_group_name=subnet_group.name,
            vpc_security_group_ids=[security_group.id],
            # Monitoring
            # Use `RDS service-linked role` for publishing logs to CloudWatch Logs
            enabled_cloudwatch_logs_exports=["audit", "error", "general", "slowquery"],
            **kwargs,
        )

    def create_instance(self, resource_name: str, **kwargs) -> ServerlessV2Instance:
        return ServerlessV2Instance(resource_name, cluster=self, **kwargs)
