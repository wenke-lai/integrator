from pulumi_aws import dynamodb

from diagrams.eraser import cloud_architecture as diagram


class Table(dynamodb.Table):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new DynamoDB Table.

        Args:
            name (str): The name of the DynamoDB Table.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/dynamodb/table/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name, icon="aws-dynamodb")
