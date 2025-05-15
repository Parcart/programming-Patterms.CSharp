import re
from abc import abstractmethod, ABC
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

# class TwitterUserService:
#     def __init__(self):
#         self._client = TwitterClient()
#
#     def get_user_info(self, page_url: str) -> UserInfo:
#         """
#         Этот метод содержит дублирование с VkUserService.GetUserInfo
#         необходимо избавиться от дублирования (см. задание)
#         """
#         regex = re.compile(r"twitter.com/(.*)")
#         user_name = regex.match(page_url).group(0)
#
#         user_id = self._get_user_id(user_name)
#
#         subscribers = self._client.get_subscribers(user_id)
#
#         friends = [
#             UserInfo(
#                 user_id=str(c.user_id),
#                 name=self._client.get_user_name_by_id(c.user_id)
#             )
#             for c in subscribers
#         ]
#
#         return UserInfo(
#             name=user_name,
#             user_id=str(user_id),
#             friends=friends
#         )
#
#     def _get_user_id(self, user_name: str) -> int:
#         """
#         Нет необходимости менять этот метод, достаточно просто переиспользовать
#         Реализация его не важна, стоит полагаться только на его внешний интерфейс
#         """
#         # TODO: Return userId from userName
#         return 0
#
#
# class VkUserService:
#     def __init__(self):
#         pass
#
#     def get_user_info(self, page_url: str) -> UserInfo:
#         """
#         Этот метод содержит дублирование с TwitterUserService.GetUserInfo
#         необходимо избавиться от дублирования (см. задание)
#         """
#         user_id = self._parse(page_url)
#         result = UserInfo()
#         result.name = self._get_name(user_id)
#         result.user_id = user_id
#
#         users = self._get_friends_by_id(result.user_id)
#         friends = self._convert_to_user_info(users)
#         result.friends = friends
#         return result
#
#     def _get_name(self, user_id: str) -> str:
#         """
#         Нет необходимости менять этот метод, достаточно просто переиспользовать
#         Реализация его не важна, стоит полагаться только на его внешний интерфейс
#         """
#         return "NAME"
#
#     def _get_friends_by_id(self, user_id: str) -> list[VkUser]:
#         """
#         Нет необходимости менять этот метод, достаточно просто переиспользовать
#         Реализация его не важна, стоит полагаться только на его внешний интерфейс
#         """
#         return []
#
#     def _parse(self, page_url: str) -> str:
#         """
#         Нет необходимости менять этот метод, достаточно просто переиспользовать
#         Реализация его не важна, стоит полагаться только на его внешний интерфейс
#         """
#         return "USER_ID"
#
#     def _convert_to_user_info(self, friends: list[VkUser]) -> list[UserInfo]:
#         """
#         Нет необходимости менять этот метод, достаточно просто переиспользовать
#         Реализация его не важна, стоит полагаться только на его внешний интерфейс
#         """
#         return []

# В целом в питоне нету смысла делать эти абстрактые классы, это для позеров
class SocialNetworkService:
    """
    Абстрактно не позерский базовый класс, содержащий общий алгоритм получения UserInfo
    """

    def get_user_info(self, page_url: str) -> UserInfo:
        # 1. Получаем идентификатор пользователя
        user_id = self._parse_user_id(page_url)

        # 2. Получаем имя пользователя
        user_name = self._get_user_name(user_id)

        # 3. Получаем друзей/подписчиков
        friends = self._get_friends(user_id)

        # 4. Конвертируем в общий формат
        converted_friends = self._convert_friends(friends)

        # 5. Собираем результат
        return UserInfo(
            name=user_name,
            user_id=user_id,
            friends=converted_friends
        )

    def _parse_user_id(self, page_url: str) -> str:
        raise NotImplementedError()

    def _get_user_name(self, user_id: str) -> str:
        raise NotImplementedError()

    def _get_friends(self, user_id: str):
        raise NotImplementedError()

    def _convert_friends(self, friends) -> List[UserInfo]:
        raise NotImplementedError()


class TwitterUserService(SocialNetworkService):
    def __init__(self):
        self._client = TwitterClient()

    def _parse_user_id(self, page_url: str) -> str:
        regex = re.compile(r"twitter.com/(.*)")
        user_name = regex.match(page_url).group(0)
        return str(self._client.get_user_id_by_name(user_name))

    def _get_user_name(self, user_id: str) -> str:
        return self._client.get_user_name_by_id(int(user_id))

    def _get_friends(self, user_id: str):
        return self._client.get_subscribers(int(user_id))

    def _convert_friends(self, friends) -> List[UserInfo]:
        return [
            UserInfo(
                user_id=str(f.user_id),
                name=self._client.get_user_name_by_id(f.user_id)
            )
            for f in friends
        ]


class VkUserService(SocialNetworkService):
    def __init__(self):
        pass

    def _parse_user_id(self, page_url: str) -> str:
        return self._parse(page_url)

    def _get_user_name(self, user_id: str) -> str:
        return self._get_name(user_id)

    def _get_friends(self, user_id: str):
        return self._get_friends_by_id(user_id)

    def _convert_friends(self, friends) -> List[UserInfo]:
        return self._convert_to_user_info(friends)

    # Оригинальные методы VkUserService
    def _get_name(self, user_id: str) -> str:
        return "NAME"

    def _get_friends_by_id(self, user_id: str) -> List[VkUser]:
        return []

    def _parse(self, page_url: str) -> str:
        return "USER_ID"

    def _convert_to_user_info(self, friends: List[VkUser]) -> List[UserInfo]:
        return []