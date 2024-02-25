from pulumi_aws import opensearch

from diagrams.eraser import cloud_architecture as diagram


class Domain(opensearch.Domain):

    def __init__(self, name: str, **kwargs) -> None:
        """Create a new OpenSearch Domain.

        Args:
            name (str): The name of the OpenSearch Domain.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/opensearch/domain/#inputs)
        """

        # log_group = cloudwatch.LogGroup()
        # document = iam.Document()
        # policy = cloudwatch.LogResourcePolicy()

        super().__init__(
            name,
            # cloudwatch_log_group_arn=log_group.arn,
            **kwargs,
        )
        self.diagram = diagram.Node(name, icon="aws-opensearch-service")
