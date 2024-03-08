from pulumi_aws import rds

from diagrams.eraser import cloud_architecture as diagram


class Cluster(rds.Cluster):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new RDS Cluster.

        Args:
            resource_name (str): The name of the RDS Cluster.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/rds/cluster/#inputs)
        """

        super().__init__(resource_name, **kwargs)

        self.diagram = diagram.Node(resource_name, icon="aws-rds")
