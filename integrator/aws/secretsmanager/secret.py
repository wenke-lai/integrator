from pulumi_aws import secretsmanager


class Secret(secretsmanager.Secret):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new Secret.

        Args:
            resource_name (str): The name of the Secret.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/secretsmanager/secret/#inputs)
        """

        super().__init__(resource_name, **kwargs)
