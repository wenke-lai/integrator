from pulumi_aws import iam


class User(iam.User):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new IAM User.

        Args:
            resource_name (str): The name of the IAM User.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/iam/user/#inputs)
        """

        super().__init__(resource_name, **kwargs)
