from pulumi_aws import cloudfront

from diagrams.eraser import cloud_architecture as diagram


class OriginRequestPolicy(cloudfront.OriginRequestPolicy):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new Origin Request Policy.

        Args:
            name (str): The name of the Origin Request Policy.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cloudfront/originrequestpolicy/#inputs)
        """
        super().__init__(name, **kwargs)

        self.diagram = diagram.Node(
            name + "origin-request-policy", icon="aws-cloudfront"
        )
