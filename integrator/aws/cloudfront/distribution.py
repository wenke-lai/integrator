from pulumi_aws import cloudfront

from diagrams.eraser import cloud_architecture as diagram


class Distribution(cloudfront.Distribution):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new CloudFront Distribution.

        Args:
            name (str): The name of the CloudFront Distribution.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cloudfront/distribution/#inputs)
        """
        super().__init__(name, **kwargs)

        self.diagram = diagram.Node(name, icon="aws-cloudfront")
