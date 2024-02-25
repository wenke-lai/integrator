from pulumi_aws import ecs

from diagrams.eraser import cloud_architecture as diagram


class TaskDefinition(ecs.TaskDefinition):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new ECS Task Definition.
        Args:
            name (str): The name of the ECS Task Definition.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ecs/taskdefinition/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagarm = diagram.Node(
            name + "task-definition", icon="aws-elastic-container-service"
        )
