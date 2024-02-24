from pulumi_aws import cloudfront

from diagrams.eraser import cloud_architecture as diagram


class OriginAccessControl(cloudfront.OriginAccessControl):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new Origin Access Control.

        Args:
            name (str): The name of the Origin Access Control.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cloudfront/originaccesscontrol/#inputs)
        """
        super().__init__(name, **kwargs)

        self.diagram = diagram.Node(
            name + "origin-access-control", icon="aws-cloudfront"
        )
