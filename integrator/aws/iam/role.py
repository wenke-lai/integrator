import json

import pulumi
from pulumi_aws import iam

from .policy import Policy


class Role(iam.Role):
    def __init__(self, resource_name: str, assume_role_policy: str, **kwargs) -> None:
        """Create a new IAM Role.

        Args:
            resource_name (str): The name of the IAM Role.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/iam/role/#inputs)
        """
        super().__init__(
            resource_name,
            assume_role_policy=assume_role_policy,
            **kwargs,
        )

    def create_policy(
        self,
        resource_name: str,
        statements: list[iam.GetPolicyDocumentStatementArgs | dict],
        **kwargs,
    ) -> Policy:
        policy = Policy(
            resource_name,
            statements=statements,
            opts=pulumi.ResourceOptions(parent=self),
            **kwargs,
        )
        self.attach(resource_name, policy)
        return policy

    def attach(self, resource_name: str, policy: iam.Policy) -> None:
        iam.RolePolicyAttachment(
            resource_name,
            role=self.name,
            policy_arn=policy.arn,
            opts=pulumi.ResourceOptions(parent=self),
        )


class InstanceRole(Role):
    service: str = "ec2.amazonaws.com"

    def __init__(self, resource_name: str, **kwargs) -> None:
        assume_role_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "sts:AssumeRole",
                    "Effect": "Allow",
                    "Principal": {"Service": self.service},
                }
            ],
        }

        super().__init__(
            resource_name, assume_role_policy=json.dumps(assume_role_policy), **kwargs
        )

    def create_instance_profile(
        self, resource_name: str, **kwargs
    ) -> iam.InstanceProfile:
        """Create a new IAM Instance Profile using this Role.

        Args:
            resource_name (str): The name of the IAM Instance Profile.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/iam/instanceprofile/#inputs)

        Returns:
            iam.InstanceProfile: The new IAM Instance Profile.
        """
        kwargs.setdefault("opts", pulumi.ResourceOptions(parent=self))
        return iam.InstanceProfile(resource_name, role=self.name, **kwargs)
