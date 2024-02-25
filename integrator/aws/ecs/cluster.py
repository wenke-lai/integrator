from pulumi_aws import ecs

from diagrams.eraser import cloud_architecture as diagram

from .task_definition import TaskDefinition


class Cluster(ecs.Cluster):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new ECS Cluster.

        Args:
            name (str): The name of the ECS Cluster.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ecs/cluster/#inputs)
        """
        super().__init__(name, **kwargs)

        self.diagram = diagram.Group(name, icon="aws-elastic-container-service")

    def create_task_definition(self, name: str, **kwargs) -> TaskDefinition:
        """Create a new ECS Task Definition.

        Args:
            name (str): The name of the ECS Task Definition.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ecs/taskdefinition/#inputs)
        """
        task_definition = TaskDefinition(name, **kwargs)
        self.diagram.append(task_definition.diagram)
        return task_definition
