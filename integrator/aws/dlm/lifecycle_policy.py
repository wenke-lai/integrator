from pulumi_aws import dlm


class LifecyclePolicy(dlm.LifecyclePolicy):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new DLM Lifecycle Policy.

        Args:
            resource_name (str): The name of the DLM Lifecycle Policy.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/dlm/lifecyclepolicy/#inputs)
        """
        super().__init__(resource_name, **kwargs)
