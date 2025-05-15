import re
from typing import List


from dataclasses import dataclass, field

class VkUser:
    """
    Реализация его не важна, стоит полагаться только на его внешний интерфейс
    """
    pass

@dataclass
class UserInfo:
    """
    Нет необходимости менять этот класс
    """
    name: str = ""
    user_id: str = ""
    friends: list['UserInfo'] = field(default_factory=list)

class TwitterUserService:
    def __init__(self):
        self._client = TwitterClient()

    def get_user_info(self, page_url: str) -> UserInfo:
        """
        Этот метод содержит дублирование с VkUserService.GetUserInfo
        необходимо избавиться от дублирования (см. задание)
        """
        regex = re.compile(r"twitter.com/(.*)")
        user_name = regex.match(page_url).group(0)

        user_id = self._get_user_id(user_name)

        subscribers = self._client.get_subscribers(user_id)

        friends = [
            UserInfo(
                user_id=str(c.user_id),
                name=self._client.get_user_name_by_id(c.user_id)
            )
            for c in subscribers
        ]

        return UserInfo(
            name=user_name,
            user_id=str(user_id),
            friends=friends
        )

    def _get_user_id(self, user_name: str) -> int:
        """
        Нет необходимости менять этот метод, достаточно просто переиспользовать
        Реализация его не важна, стоит полагаться только на его внешний интерфейс
        """
        # TODO: Return userId from userName
        return 0


class VkUserService:
    def __init__(self):
        pass

    def get_user_info(self, page_url: str) -> UserInfo:
        """
        Этот метод содержит дублирование с TwitterUserService.GetUserInfo
        необходимо избавиться от дублирования (см. задание)
        """
        user_id = self._parse(page_url)
        result = UserInfo()
        result.name = self._get_name(user_id)
        result.user_id = user_id

        users = self._get_friends_by_id(result.user_id)
        friends = self._convert_to_user_info(users)
        result.friends = friends
        return result

    def _get_name(self, user_id: str) -> str:
        """
        Нет необходимости менять этот метод, достаточно просто переиспользовать
        Реализация его не важна, стоит полагаться только на его внешний интерфейс
        """
        return "NAME"

    def _get_friends_by_id(self, user_id: str) -> list[VkUser]:
        """
        Нет необходимости менять этот метод, достаточно просто переиспользовать
        Реализация его не важна, стоит полагаться только на его внешний интерфейс
        """
        return []

    def _parse(self, page_url: str) -> str:
        """
        Нет необходимости менять этот метод, достаточно просто переиспользовать
        Реализация его не важна, стоит полагаться только на его внешний интерфейс
        """
        return "USER_ID"

    def _convert_to_user_info(self, friends: list[VkUser]) -> list[UserInfo]:
        """
        Нет необходимости менять этот метод, достаточно просто переиспользовать
        Реализация его не важна, стоит полагаться только на его внешний интерфейс
        """
        return []