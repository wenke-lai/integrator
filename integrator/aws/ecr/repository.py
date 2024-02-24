from pulumi_aws import ecr

from diagrams.eraser import cloud_architecture as diagram


class Repository(ecr.Repository):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new ECR Repository.

        Args:
            name (str): The name of the ECR Repository.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ecr/repository/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name, icon="aws-elastic-container-registry")
