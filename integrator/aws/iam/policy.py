from pulumi_aws import iam

from diagrams.eraser import cloud_architecture as diagram


class Policy(iam.Policy):
    def __init__(
        self,
        resource_name: str,
        statements: list[iam.GetPolicyDocumentStatementArgs | dict],
        **kwargs
    ) -> None:
        """Create a new IAM Policy.

        Args:
            resource_name (str): The name of the IAM Policy.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/iam/policy/#inputs)
        """
        document = iam.get_policy_document(statements=statements)
        super().__init__(resource_name, policy=document.json, **kwargs)
        self.diagram = diagram.Node(resource_name, icon="aws-iam-identity-center")
