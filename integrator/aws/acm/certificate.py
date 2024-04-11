from typing import Any, Literal

from pulumi_aws import acm, get_arn

from diagrams.eraser import cloud_architecture as diagram


class ExistingCertificate:
    def __init__(self, resource_name: str, arn: str, **kwargs) -> None:
        """Look up Existing Certificate Resource

        Args:
            resource_name (str): The name of the certificate.
            arn (str): The ARN of the certificate.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/acm/certificate/#look-up)
        """
        self._resource = acm.Certificate.get(resource_name, arn, **kwargs)

        self.diagram = diagram.Node(resource_name, icon="aws-certificate-manager")

    def __getattr__(self, name: str) -> Any:
        return getattr(self._resource, name)

    @property
    def shortcut(self) -> str:
        arn = get_arn(self._resource.arn)
        certificate_id = arn.resource.split("/")[-1]
        url = f"https://{arn.region}.console.aws.amazon.com/acm/home"
        return f"{url}?region={arn.region}#/certificates/{certificate_id}"

    @property
    def price(self) -> float:
        """Return the price per monthly for the resource in USD.

        Public SSL/TLS certificates provisioned through AWS Certificate Manager are free
        """
        return 0.0


class Certificate(acm.Certificate):

    @staticmethod
    def get(resource_name: str, arn: str, **kwargs) -> ExistingCertificate:
        return ExistingCertificate(resource_name, arn, **kwargs)

    def __init__(
        self,
        resource_name: str,
        domain_name: str,
        validation_method: Literal["DNS", "EMAIL"] = "DNS",
        **kwargs,
    ) -> None:
        """Create a new Certificate.

        Args:
            resource_name (str): The name of the certificate.
            domain_name (str): The domain name to use for the certificate.
            validation_method (Literal["DNS", "EMAIL"], optional): The method to use for validation. Defaults to "DNS".
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/acm/certificate/#inputs)
        """

        super().__init__(
            resource_name,
            domain_name=domain_name,
            validation_method=validation_method,
            **kwargs,
        )

        self.diagram = diagram.Node(resource_name, icon="aws-certificate-manager")

    @property
    def shortcut(self) -> str:
        arn = get_arn(self.arn)
        certificate_id = arn.resource.split("/")[-1]
        url = f"https://{arn.region}.console.aws.amazon.com/acm/home"
        return f"{url}?region={arn.region}#/certificates/{certificate_id}"

    @property
    def price(self) -> float:
        """Return the price per monthly for the resource in USD.

        Public SSL/TLS certificates provisioned through AWS Certificate Manager are free
        """
        return 0.0
