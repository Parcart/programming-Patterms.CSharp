# Этот код моделирует класс InstagramClient, который нельзя менять по условиям задания.
# Он имитирует внешний компонент или библиотеку для взаимодействия с Instagram.
from abc import ABC, abstractmethod


class InstagramUser: # Создал класс InstagramUser
    """
    Представляет пользователя Instagram.
    В реальном проекте этот класс содержал бы информацию о пользователе, такую как имя, ID и т.д.
    """
    def __init__(self, username: str): # Добавил конструктор что бы возвращать обьект а не пустой массив
        self.username = username

class InstagramClient:
    """
    Клиент для взаимодействия с Instagram API.
    (Имитация внешней библиотеки)
    """

    def get_subscribers(self, user_name: str) -> list[InstagramUser]:
        """
        Возвращает список подписчиков указанного пользователя Instagram.

        Args:
            user_name (str): Имя пользователя Instagram.

        Returns:
            list[InstagramUser]: Список подписчиков (в данном случае всегда пустой).
        """
        return []


class TwitterUser:
    def __init__(self, username: str, user_id: int):
        self.username = username
        self.user_id = user_id

class TwitterClient:
    """
    Клиент для взаимодействия с Twitter API.
    (Имитация внешней библиотеки)
    """

    def get_user_id_by_name(self, name: str) -> int:
        """
        Возвращает ID пользователя Twitter по его имени.

        Args:
            name (str): Имя пользователя Twitter.

        Returns:
            int: ID пользователя (в данном случае всегда 1).
        """
        return 1

    def get_user_name_by_id(self, id: int) -> str:
        """
        Возвращает имя пользователя Twitter по его ID.

        Args:
            id (int): ID пользователя Twitter.

        Returns:
            str: Имя пользователя (в данном случае всегда пустая строка).
        """
        return ""

    def get_subscribers(self, user_id: int) -> list[TwitterUser]:
        """
        Возвращает список подписчиков указанного пользователя Twitter.

        Args:
            user_id (int): ID пользователя Twitter.

        Returns:
            list[TwitterUser]: Список подписчиков (в данном случае всегда пустой).
        """
        return []

from enum import Enum

class SocialNetwork(Enum):
    """
    Перечисление, представляющее социальные сети.
    """
    Instagram = 1
    Twitter = 2

# Имитация класса SocialNetworkUser из C# в Python.
# Неизменяемый класс для представления пользователя социальной сети.

class SocialNetworkUser:
    """
    Представляет пользователя социальной сети.
    Имитация C# класса.  Содержит только имя пользователя.
    """
    def __init__(self, user_name: str):
        """
        Инициализирует объект SocialNetworkUser.

        Args:
            user_name (str): Имя пользователя.
        """
        self.user_name = user_name


# РЕШЕНИЕ начинается от сюда да
# 1. Создаем интерфейс для работы с социальными сетями
class ISocialNetworkClient:
    def get_subscribers(self, username: str) -> list[SocialNetworkUser]:
        raise NotImplementedError("Я не позер")


# 2. Реализуем адаптеры для каждой социальной сети
class TwitterClientAdapter(ISocialNetworkClient):
    def __init__(self, client: TwitterClient):
        self._client = client

    def get_subscribers(self, username: str) -> list[SocialNetworkUser]:
        user_id = self._client.get_user_id_by_name(username)
        subscribers = self._client.get_subscribers(user_id)
        return [SocialNetworkUser(sub.user_id) for sub in subscribers]


class InstagramClientAdapter(ISocialNetworkClient):
    def __init__(self, client: InstagramClient):
        self._client = client

    def get_subscribers(self, username: str) -> list[SocialNetworkUser]:
        subscribers = self._client.get_subscribers(username)
        return [SocialNetworkUser(sub.username) for sub in subscribers]


# 3. Модифицируем SubscriberViewer
class SubscriberViewer:
    def __init__(self):
        # Инициализируем клиенты (можно вынести в конфигурацию)
        self._clients = {
            SocialNetwork.Twitter: TwitterClientAdapter(TwitterClient()),
            SocialNetwork.Instagram: InstagramClientAdapter(InstagramClient())
        }

    def get_subscribers(self, user_name: str, network_type: SocialNetwork) -> list[SocialNetworkUser]:
        client = self._clients.get(network_type)
        if not client:
            raise ValueError(f"Unsupported social network: {network_type}")

        return client.get_subscribers(user_name)

    def register_client(self, network_type: SocialNetwork, client: ISocialNetworkClient):
        """Метод для добавления новых социальных сетей без изменения основного кода"""
        self._clients[network_type] = client