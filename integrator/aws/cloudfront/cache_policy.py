from pulumi_aws import cloudfront

from diagrams.eraser import cloud_architecture as diagram


class CachePolicy(cloudfront.CachePolicy):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new Cache Policy.

        Args:
            name (str): The name of the Cache Policy.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cloudfront/cachepolicy/#inputs)
        """
        super().__init__(name, **kwargs)

        self.diagram = diagram.Node(name + "-cache-policy", icon="aws-cloudfront")
