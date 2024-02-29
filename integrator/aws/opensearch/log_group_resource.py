from typing import Optional

from pulumi_aws import iam

from ..cloudwatch import LogGroup, LogResourcePolicy


class ElasticsearchLogResourcePolicy(LogResourcePolicy):

    def __init__(
        self,
        name: str,
        groups: list[LogGroup],
        policy_name: Optional[str] = None,
        **kwargs,
    ) -> None:
        """Create a new Log Resource Policy for Elasticsearch."""

        document = iam.get_policy_document(
            statements=[
                iam.GetPolicyDocumentStatementArgs(
                    effect="Allow",
                    principals=[
                        iam.GetPolicyDocumentStatementPrincipalArgs(
                            type="Service", identifiers=["es.amazonaws.com"]
                        )
                    ],
                    actions=[
                        "logs:CreateLogStream",
                        "logs:PutLogEvents",
                        "logs:PutLogEventsBatch",
                    ],
                    resources=[
                        group.arn.apply(lambda arn: f"{arn}:*") for group in groups
                    ],
                )
            ]
        )

        super().__init__(
            name,
            policy_name=policy_name or name,
            policy_document=document.json,
            **kwargs,
        )

        for group in groups:
            self.diagram.append(group.diagram)
