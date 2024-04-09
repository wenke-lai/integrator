from __future__ import annotations

import typing

from pulumi import Config, ResourceOptions
from pulumi_aws import route53

from diagrams.eraser import cloud_architecture as diagram

from .record import ARecord, CNameRecord

if typing.TYPE_CHECKING:
    from ..ec2 import Vpc


class ExistingZone:

    def __init__(self, resource_name: str, zone_id: str, **kwargs) -> None:
        """Look up Existing Zone Resource

        Args:
            resource_name (str): The name of the Route53 Zone.
            zone_id (str): The ID of the Route53 Zone.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/route53/zone/#look-up)
        """

        self._resource = route53.Zone.get(
            resource_name=resource_name, id=zone_id, **kwargs
        )

    @property
    def shortcut(self) -> str:
        region = Config("aws").get("region", default="us-east-1")
        url = "https://us-east-1.console.aws.amazon.com/route53/v2/hostedzones"

        return self._resource.zone_id.apply(
            lambda zone_id: f"{url}?region={region}#ListRecordSets/{zone_id}"
        )

    def create_a_record(
        self, resource_name: str, name: str, record: str, **kwargs
    ) -> ARecord:
        """Create a new A record

        Args:
            resource_name (str): The name of the A record.
            name (str): The name of the A record.
            record (str): The IP address of the A record.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/route53/record/#inputs)

        Returns:
            ARecord: The A record resource
        """

        opts = ResourceOptions(parent=self._resource)
        opts.merge(kwargs.pop("opts", None))

        return ARecord(
            resource_name=resource_name,
            name=name,
            zone=self._resource,
            record=record,
            opts=opts,
            **kwargs,
        )

    def create_cname_record(
        self, resource_name: str, name: str, record: str, **kwargs
    ) -> CNameRecord:
        """Create a new CNAME record

        Args:
            resource_name (str): The name of the CNAME record.
            name (str): The name of the CNAME record.
            record (str): The CNAME record.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/route53/record/#inputs)

        Returns:
            CNameRecord: The CNAME record resource
        """
        opts = ResourceOptions(parent=self._resource)
        opts.merge(kwargs.pop("opts", None))

        return CNameRecord(
            resource_name=resource_name,
            name=name,
            zone=self._resource,
            record=record,
            opts=opts,
            **kwargs,
        )


class Zone(route53.Zone):

    @staticmethod
    def get(resource_name: str, zone_id: str, **kwargs) -> ExistingZone:
        return ExistingZone(resource_name=resource_name, zone_id=zone_id, **kwargs)

    def __init__(self, resource_name: str, domain: str, **kwargs) -> None:
        """Create a new Route53 Zone.

        Args:
            resource_name (str): The name of the Route53 Zone.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/route53/zone/#inputs)
        """

        super().__init__(resource_name, name=domain, **kwargs)

        self.diagram = diagram.Node(resource_name, icon="aws-route53")

    @property
    def shortcut(self) -> str:
        region = Config("aws").get("region", default="us-east-1")
        url = "https://us-east-1.console.aws.amazon.com/route53/v2/hostedzones"

        return self.zone_id.apply(
            lambda zone_id: f"{url}?region={region}#ListRecordSets/{zone_id}"
        )

    def create_a_record(
        self, resource_name: str, name: str, record: str, **kwargs
    ) -> ARecord:
        """Create a new A record

        Args:
            resource_name (str): The name of the A record.
            name (str): The name of the A record.
            record (str): The IP address of the A record.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/route53/record/#inputs)

        Returns:
            ARecord: The A record resource
        """

        opts = ResourceOptions(parent=self._resource)
        opts.merge(kwargs.pop("opts", None))

        return ARecord(
            resource_name=resource_name,
            name=name,
            zone=self,
            record=record,
            opts=opts,
            **kwargs,
        )

    def create_cname_record(
        self, resource_name: str, name: str, record: str, **kwargs
    ) -> CNameRecord:
        """Create a new CNAME record

        Args:
            resource_name (str): The name of the CNAME record.
            name (str): The name of the CNAME record.
            record (str): The CNAME record.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/route53/record/#inputs)

        Returns:
            CNameRecord: The CNAME record resource
        """

        opts = ResourceOptions(parent=self._resource)
        opts.merge(kwargs.pop("opts", None))

        return CNameRecord(
            resource_name=resource_name,
            name=name,
            zone=self,
            record=record,
            opts=opts,
            **kwargs,
        )


class PrivateZone(Zone):
    def __init__(self, resource_name: str, domain: str, vpc: Vpc, **kwargs) -> None:
        """Create a new private route53 zone

        Args:
            resource_name (str): The name of the Route53 Zone.
            domain (str): The domain name of the Route53 Zone.
            vpc (Vpc): The VPC to associate with the Route53 Zone.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/route53/zone/#inputs)
        """

        super().__init__(
            resource_name,
            name=domain,
            vpcs=[route53.ZoneVpcArgs(vpc_id=vpc.id)],
            **kwargs,
        )
