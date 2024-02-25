from pulumi_aws import lambda_

from diagrams.eraser import cloud_architecture as diagram


class Function(lambda_.Function):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new Lambda Function.

        Args:
            name (str): The name of the Lambda Function.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/lambda/function/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name, icon="aws-lambda")
