from pulumi_aws import lambda_


class Function(lambda_.Function):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new Lambda Function.

        Args:
            resource_name (str): The name of the Lambda Function.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/lambda/function/#inputs)
        """

        super().__init__(resource_name, **kwargs)
