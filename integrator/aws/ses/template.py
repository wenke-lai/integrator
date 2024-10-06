from pulumi_aws import ses


class Template(ses.Template):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new AWS SES Template.

        Args:
            resource_name (str): The name of the AWS SES Template.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ses/template/#inputs)
        """

        super().__init__(resource_name, **kwargs)
