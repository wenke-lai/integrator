from pulumi_aws import kms


class Key(kms.Key):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new KMS Key.

        Args:
            resource_name (str): The name of the KMS Key.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/kms/key/#inputs)
        """

        super().__init__(resource_name, **kwargs)
