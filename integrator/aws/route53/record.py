from pulumi_aws import route53

from diagrams.eraser import cloud_architecture as diagram


class Record(route53.Record):

    def __init__(self, name: str, **kwargs) -> None:
        """Create a new Route53 Record.

        Args:
            name (str): The name of the Route53 Record.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/route53/record/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name, icon="aws-route53")
