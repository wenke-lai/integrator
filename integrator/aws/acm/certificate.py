from typing import Literal

from pulumi_aws.aws import acm

from diagrams.eraser import cloud_architecture as diagram


class Certificate(acm.Certificate):

    def __init__(
        self,
        name: str,
        domain_name: str,
        validation_method: Literal["DNS", "EMAIL"] = "DNS",
        **kwargs
    ) -> None:
        """Create a new Certificate.

        Args:
            name (str): The name of the certificate.
            domain_name (str): The domain name to use for the certificate.
            validation_method (Literal["DNS", "EMAIL"], optional): The method to use for validation. Defaults to "DNS".
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/acm/certificate/#inputs)
        """

        super().__init__(
            name,
            domain_name=domain_name,
            validation_method=validation_method,
            **kwargs,
        )

        self.diagram = diagram.Node(name, icon="aws-certificate-manager")
