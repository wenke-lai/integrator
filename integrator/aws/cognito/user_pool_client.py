from pulumi_aws import cognito


class UserPoolClient(cognito.UserPoolClient):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new Cognito User Pool Client.

        Args:
            resource_name (str): The name of the Cognito User Pool Client.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cognito/userpoolclient/#inputs)
        """

        super().__init__(resource_name, **kwargs)
