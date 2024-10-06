from pulumi_aws import dynamodb


class Table(dynamodb.Table):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new DynamoDB Table.

        Args:
            resource_name (str): The name of the DynamoDB Table.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/dynamodb/table/#inputs)
        """
        super().__init__(resource_name, **kwargs)
