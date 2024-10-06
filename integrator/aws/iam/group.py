from pulumi_aws import iam


class Group(iam.Group):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new IAM Group.

        Args:
            resource_name (str): The name of the IAM Group.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/iam/group/#inputs)
        """
        super().__init__(resource_name, **kwargs)
