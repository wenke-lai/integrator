from pulumi_aws import ec2

from diagrams.eraser import cloud_architecture as diagram


class SecurityGroup(ec2.SecurityGroup):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new EC2 Security Group.

        Args:
            name (str): The name of the EC2 Security Group.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/securitygroup/#inputs)
        """
        super().__init__(name, **kwargs)
        self.diagram = diagram.Node(name, icon="aws-ec2")

    def add_ingress_rule(self, name: str, **kwargs) -> None:
        """Add an ingress rule to the Security Group.

        Args:
            rule (ec2.SecurityGroupRule): The rule to add.
        """
        rule = ec2.SecurityGroupRule(name, **kwargs)
        return rule

    def add_egress_rule(self, name: str, **kwargs) -> None:
        """Add an egress rule to the Security Group.

        Args:
            rule (ec2.SecurityGroupRule): The rule to add.
        """
        rule = ec2.SecurityGroupRule(name, **kwargs)
        return rule
