from abc import ABC, abstractmethod

class IDatabaseSaver(ABC):
    """
    Интерфейс для сохранения в БД
    """
    @abstractmethod
    def save_data(self, data: object) -> None:
        pass


class DatabaseSaver(IDatabaseSaver):
    """
    Сохраняет в БД (реализация интерфейса IDatabaseSaver)
    """
    def save_data(self, data: object) -> None:
        """
        Сохранение данных в БД
        """
        # Реальная реализация сохранения в БД
        print(f"Сохранение данных в БД: {data}")


class CacheUpdater:
    """
    Обновляет кэш
    """
    def update_cache(self) -> None:
        """
        Обновление кэша
        """
        print("Обновление кэша")


class MailSender:
    """
    Отправляет письмо на email
    """
    def send(self, email: str) -> None:
        """
        Отправка письма на email
        """
        print(f"Отправка письма на email: {email}")
