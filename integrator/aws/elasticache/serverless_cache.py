from typing import TYPE_CHECKING, Literal

from pulumi_aws import elasticache

if TYPE_CHECKING:
    from integrator.aws.ec2.security_group import SecurityGroup
    from integrator.aws.ec2.subnet import Subnet

    from .user_group import UserGroup


class ServerlessCache(elasticache.ServerlessCache):
    def __init__(
        self,
        resource_name: str,
        engine: Literal["redis", "memcached"],
        **kwargs,
    ):
        super().__init__(
            resource_name,
            engine=engine,
            **kwargs,
        )


class ServerlessRedis(ServerlessCache):
    def __init__(
        self,
        resource_name: str,
        security_group: SecurityGroup,
        subnets: list[Subnet],
        cache_usage_limits: dict[str, int],
        major_engine_version: str = "7",
        daily_snapshot_time: str = "1",
        snapshot_retention_limit: int = 30,
        user_group: UserGroup | None = None,
        **kwargs,
    ):
        user_group_id = None
        if user_group:
            user_group_id = user_group.id

        super().__init__(
            resource_name,
            security_group_ids=[security_group.id],
            subnet_ids=[subnet.id for subnet in subnets],
            user_group_id=user_group_id,
            cache_usage_limits=cache_usage_limits,
            engine="redis",
            major_engine_version=major_engine_version,
            daily_snapshot_time=daily_snapshot_time,
            snapshot_retention_limit=snapshot_retention_limit,
            **kwargs,
        )
