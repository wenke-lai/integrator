from pulumi_aws import route53

from diagrams.eraser import cloud_architecture as diagram


class Zone(route53.Zone):

    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new Route53 Zone.

        Args:
            resource_name (str): The name of the Route53 Zone.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/route53/zone/#inputs)
        """

        super().__init__(resource_name, **kwargs)

        self.diagram = diagram.Node(resource_name, icon="aws-route53")
