from typing import Optional

from pulumi_aws import ecr


class Repository(ecr.Repository):
    def __init__(
        self,
        resource_name: str,
        name: Optional[str] = None,
        **kwargs,
    ) -> None:
        """Create a new ECR Repository.

        Args:
            resource_name (str): The name of this resource.
            name (Optional[str]): Name of the repository. Defaults to None.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ecr/repository/#inputs)
        """
        super().__init__(resource_name, name=name, **kwargs)
