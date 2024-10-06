from pulumi_aws import cognito


class UserPoolDomain(cognito.UserPoolDomain):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new Cognito User Pool Domain.

        Args:
            resource_name (str): The name of the Cognito User Pool Domain.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cognito/userpooldomain/#inputs)
        """

        super().__init__(resource_name, **kwargs)
