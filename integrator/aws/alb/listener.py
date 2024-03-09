from __future__ import annotations

from pulumi_aws import alb

from diagrams.eraser import cloud_architecture as diagram


class DefaultAction(alb.ListenerDefaultActionArgs):

    @classmethod
    def create_forward(cls, target_group_arn: str) -> DefaultAction:
        return cls(type="forward", target_group_arn=target_group_arn)

    @classmethod
    def create_fixed_response(cls, status_code: int, message: str) -> DefaultAction:
        return cls(
            type="fixed-response",
            fixed_response={
                "content_type": "text/plain",
                "message_body": message,
                "status_code": status_code,
            },
        )


class Listener(alb.Listener):
    def __init__(
        self,
        resource_name: str,
        load_balancer_arn: str,
        certificate_arn: str,
        default_actions: list[DefaultAction],
        port: int = 443,
        protocol: str = "HTTPS",
        ssl_policy: str = "ELBSecurityPolicy-2016-08",
        **kwargs,
    ) -> None:
        """Create a new Listener.

        Args:
            resource_name (str): The name of the listener.
            load_balancer_arn (str): The ARN of the load balancer.
            certificate_arn (str): The ARN of the certificate to use.
            default_actions (list[DefaultAction]): A list of default actions to take.
            port (int, optional): The port to listen on. Defaults to 443.
            protocol (str, optional): The protocol to use. Defaults to "HTTPS".
            ssl_policy (str, optional): The SSL policy to use. Defaults to "ELBSecurityPolicy-2016-08".
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/alb/listener/#inputs)
        """

        super().__init__(
            resource_name,
            load_balancer_arn=load_balancer_arn,
            certificate_arn=certificate_arn,
            port=port,
            protocol=protocol,
            ssl_policy=ssl_policy,
            default_actions=default_actions,
            **kwargs,
        )

        self.diagram = diagram.Node(
            resource_name + "-listener", icon="aws-elastic-load-balancing"
        )
