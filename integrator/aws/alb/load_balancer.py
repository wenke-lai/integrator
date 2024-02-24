from pulumi_aws.aws import alb

from diagrams.eraser import cloud_architecture as diagram

from .listener import DefaultAction, Listener
from .target_group import TargetGroup


class LoadBalancer(alb.LoadBalancer):
    def __init__(
        self,
        name: str,
        security_groups: list,
        subnets: list,
        internal: bool = False,
        enable_deletion_protection: bool = True,
        **kwargs,
    ) -> None:
        """Create a new LoadBalancer.

        Args:
            name (str): The name of the LoadBalancer.
            security_groups (list): A list of security groups to associate with the LoadBalancer.
            subnets (list): A list of subnets to associate with the LoadBalancer.
            internal (bool, optional): If true, the LoadBalancer will be internal. Defaults to False.
            enable_deletion_protection (bool, optional): If true, deletion protection will be enabled. Defaults to True.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/alb/loadbalancer/#inputs)
        """
        super().__init__(
            name,
            load_balancer_type="application",
            security_groups=[sg.id for sg in security_groups],
            subnets=[subnet.id for subnet in subnets],
            internal=internal,
            enable_deletion_protection=enable_deletion_protection,
            **kwargs,
        )

        self.diagram = diagram.Group(name, icon="aws-elastic-load-balancing")

    def create_target_group(
        self,
        name: str,
        vpc_id: str,
        port: int = 443,
        protocol: str = "HTTPS",
        **kwargs,
    ) -> TargetGroup:
        target_group = TargetGroup(
            name, port=port, protocol=protocol, vpc_id=vpc_id, **kwargs
        )
        self.diagram.append(target_group.diagram)
        return target_group

    def create_listener(
        self,
        name: str,
        target_group: TargetGroup,
        certificate_arn: str,
        **kwargs,
    ):
        default_action = DefaultAction.forward(target_group_arn=target_group.arn)
        listener = Listener(
            name,
            load_balancer_arn=self.arn,
            certificate_arn=certificate_arn,
            default_actions=[default_action],
            **kwargs,
        )

        self.diagram.append(listener.diagram)
        listener.diagram.edges.connect(target_group.diagram)
        return listener
