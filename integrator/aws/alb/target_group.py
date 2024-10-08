from pulumi_aws import alb


class TargetGroup(alb.TargetGroup):
    def __init__(
        self,
        resource_name: str,
        port: int = 443,
        protocol: str = "HTTPS",
        vpc_id: str = None,
        **kwargs,
    ):
        """Create a new TargetGroup.

        Args:
            resource_name (str): The name of the TargetGroup.
            port (int, optional): The port the TargetGroup will listen on. Defaults to 443.
            protocol (str, optional): The protocol the TargetGroup will use. Defaults to "HTTPS".
            vpc_id (str, optional): The VPC ID to associate with the TargetGroup. Defaults to None.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/alb/targetgroup/#inputs)
        """
        super().__init__(
            resource_name,
            port=port,
            protocol=protocol,
            vpc_id=vpc_id,
            **kwargs,
        )
