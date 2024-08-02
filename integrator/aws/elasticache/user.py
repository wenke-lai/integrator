from typing import Any

from pulumi_aws import elasticache


class UserAccessString:
    # an active user with access to all available keys and commands
    All = "on ~* +@all"


class ExistingUser:
    def __init__(self, resource_name: str, id: str, **kwargs) -> None:
        self._resource = elasticache.User.get(resource_name, id=id, **kwargs)

    def __getattr__(self, name: str) -> Any:
        return getattr(self._resource, name)


class User(elasticache.User):
    @staticmethod
    def get(resource_name: str, id: str, **kwargs) -> ExistingUser:
        return ExistingUser(resource_name, id, **kwargs)

    def __init__(self, **kwargs) -> None:
        # The current supported value is REDIS
        kwargs["engine"] = "REDIS"
        super().__init__(**kwargs)


class PasswordUser(User):
    def __init__(
        self,
        resource_name: str,
        username: str,
        password: str,
        access_string: str = UserAccessString.All,
        **kwargs,
    ) -> None:
        kwargs["authentication_mode"] = {
            "type": "password",
            "passwords": [password],
        }

        super().__init__(
            resource_name,
            user_name=username,
            access_string=access_string,
            # default
            user_id=username,
            **kwargs,
        )


class IamUser(User):
    def __init__(
        self,
        resource_name: str,
        username: str,
        access_string: str = UserAccessString.All,
        **kwargs,
    ) -> None:
        kwargs["authentication_mode"] = {
            "type": "iam",
        }

        super().__init__(
            resource_name,
            user_name=username,
            access_string=access_string,
            # default
            user_id=username,
            **kwargs,
        )
