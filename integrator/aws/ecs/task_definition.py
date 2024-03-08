from pulumi_aws import ecs

from diagrams.eraser import cloud_architecture as diagram


class TaskDefinition(ecs.TaskDefinition):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new ECS Task Definition.
        Args:
            resource_name (str): The name of the ECS Task Definition.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ecs/taskdefinition/#inputs)
        """

        super().__init__(resource_name, **kwargs)

        self.diagarm = diagram.Node(
            resource_name + "task-definition", icon="aws-elastic-container-service"
        )
