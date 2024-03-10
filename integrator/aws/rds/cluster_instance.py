from __future__ import annotations

from typing import TYPE_CHECKING

from pulumi_aws import rds

if TYPE_CHECKING:
    from .cluster import Cluster


class ClusterInstance(rds.ClusterInstance):
    def __init__(self, resource_name: str, **kwargs):
        super().__init__(resource_name, **kwargs)


class ServerlessV2Instance(ClusterInstance):
    def __init__(self, resource_name: str, cluster: Cluster, **kwargs):
        """Create a new RDS Serverless v2 Cluster Instance.

        Args:
            resource_name (str): The name of the RDS Cluster Instance.
            cluster (Cluster): The RDS Cluster object.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/rds/clusterinstance/#inputs)
        """
        super().__init__(
            resource_name,
            instance_class="db.serverless",
            cluster_identifier=cluster.id,
            engine=cluster.engine,
            engine_version=cluster.engine_version,
            **kwargs,
        )
