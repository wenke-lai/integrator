from pulumi_aws import ses

from diagrams.eraser import cloud_architecture as diagram


class Template(ses.Template):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new AWS SES Template.

        Args:
            name (str): The name of the AWS SES Template.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ses/template/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name, icon="aws-simple-email-service")
