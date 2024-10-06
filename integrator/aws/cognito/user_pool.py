from pulumi_aws import cognito

from .user_pool_client import UserPoolClient


class UserPool(cognito.UserPool):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new Cognito User Pool.

        Args:
            resource_name (str): The name of the Cognito User Pool.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/cognito/userpool/#inputs)
        """

        super().__init__(resource_name, **kwargs)

    def create_client(
        self, resource_name: str, generate_secret: bool = False, **kwargs
    ) -> UserPoolClient:
        return UserPoolClient(
            resource_name,
            user_pool_id=self.id,
            generate_secret=generate_secret,
            **kwargs,
        )
