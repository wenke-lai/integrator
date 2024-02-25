from pulumi_aws import rds

from diagrams.eraser import cloud_architecture as diagram


class Cluster(rds.Cluster):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new RDS Cluster.

        Args:
            name (str): The name of the RDS Cluster.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/rds/cluster/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name, icon="aws-rds")
