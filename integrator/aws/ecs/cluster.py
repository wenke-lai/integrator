from pulumi_aws import ecs

from .task_definition import TaskDefinition


class Cluster(ecs.Cluster):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new ECS Cluster.

        Args:
            resource_name (str): The name of the ECS Cluster.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ecs/cluster/#inputs)
        """

        super().__init__(resource_name, **kwargs)

    def create_task_definition(self, resource_name: str, **kwargs) -> TaskDefinition:
        """Create a new ECS Task Definition.

        Args:
            resource_name (str): The name of the ECS Task Definition.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ecs/taskdefinition/#inputs)
        """
        task_definition = TaskDefinition(resource_name, **kwargs)
        return task_definition
