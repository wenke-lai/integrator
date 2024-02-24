from __future__ import annotations

from pulumi_aws.aws import alb

from diagrams.eraser import cloud_architecture as diagram


class DefaultAction(alb.ListenerDefaultActionArgs):

    @classmethod
    def forward(cls, target_group_arn: str) -> DefaultAction:
        return cls(type="forward", target_group_arn=target_group_arn)

    @classmethod
    def fixed_response(cls, status_code: int, message: str) -> DefaultAction:
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
        name: str,
        load_balancer_arn: str,
        certificate_arn: str,
        default_actions: list[DefaultAction],
        port: int = 443,
        protocol: str = "HTTPS",
        ssl_policy: str = "ELBSecurityPolicy-2016-08",
        **kwargs,
    ) -> None:
        """Create a new Listener."""

        super().__init__(
            name,
            load_balancer_arn=load_balancer_arn,
            certificate_arn=certificate_arn,
            port=port,
            protocol=protocol,
            ssl_policy=ssl_policy,
            default_action=[default_actions],
            **kwargs,
        )

        self.diagram = diagram.Node(
            name + "-listener", icon="aws-elastic-load-balancing"
        )
