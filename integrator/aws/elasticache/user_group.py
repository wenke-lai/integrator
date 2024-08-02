from typing import TYPE_CHECKING

from pulumi_aws import elasticache

if TYPE_CHECKING:
    from .user import User


class UserGroup(elasticache.UserGroup):
    def __init__(
        self,
        resource_name: str,
        users: list[User] | None = None,
        **kwargs,
    ) -> None:
        kwargs["engine"] = "REDIS"

        super().__init__(
            resource_name,
            user_group_id=resource_name,
            user_ids=self._get_user_ids(resource_name, users),
            **kwargs,
        )

        self.resource_name = resource_name

    def _get_user_ids(self, resource_name: str, users: list[User] | None) -> list[str]:
        if users is None:
            default_user = User.get(resource_name, id="default")
            return [default_user.id]
        return [user.id for user in users]

    def add_user(self, resource_name: str, user: User) -> None:
        elasticache.UserGroupAssociation(
            resource_name, user_group_id=self.id, user_id=user.id
        )
