from __future__ import annotations

import typing

from pulumi_aws import route53

if typing.TYPE_CHECKING:
    from .zone import Zone


class Record(route53.Record):
    def __init__(
        self, resource_name: str, name: str, record: str, zone: Zone, **kwargs
    ) -> None:
        """Create a new Route53 Record.

        Args:
            resource_name (str): The name of the Route53 Record.
            name (str): The name of the Route53 Record.
            record (str): The record value.
            zone (Zone): The Route53 Zone to associate with the Route53 Record.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/route53/record/#inputs)
        """

        # Set the default TTL to 1 hour
        kwargs.setdefault("ttl", 3600)

        super().__init__(
            resource_name, name=name, records=[record], zone_id=zone.id, **kwargs
        )


class ARecord(Record):
    def __init__(
        self, resource_name: str, name: str, record: str, zone: Zone, **kwargs
    ) -> None:
        """Create a new A record

        Args:
            resource_name (str): The name of the A record.
            name (str): The name of the A record.
            record (str): The IP address of the A record.
            zone (Zone): The Route53 Zone to associate with the A record.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/route53/record/#inputs)
        """

        super().__init__(
            resource_name,
            name=name,
            record=record,
            zone=zone,
            type=route53.RecordType.A,
            **kwargs,
        )


class CNameRecord(Record):
    def __init__(
        self, resource_name: str, name: str, record: str, zone: Zone, **kwargs
    ) -> None:
        """Create a new CNAME record

        Args:
            resource_name (str): The name of the CNAME record.
            name (str): The name of the CNAME record.
            record (str): The CNAME record.
            zone (Zone): The Route53 Zone to associate with the CNAME record.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/route53/record/#inputs)
        """

        super().__init__(
            resource_name,
            name=name,
            record=record,
            zone=zone,
            type=route53.RecordType.CNAME,
            **kwargs,
        )
