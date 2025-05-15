from Python.Ex05.ExternalLibs import IDatabaseSaver, DatabaseSaver, MailSender, CacheUpdater


class DatabaseSaverDecorator(IDatabaseSaver):
    """
    Декоратор для добавления дополнительной функциональности к DatabaseSaver
    """

    def __init__(self, wrapped_saver: IDatabaseSaver, mail_sender: MailSender, cache_updater: CacheUpdater):
        self._wrapped_saver = wrapped_saver
        self._mail_sender = mail_sender
        self._cache_updater = cache_updater

    def save_data(self, data: object) -> None:
        # 1. Вызываем оригинальный метод сохранения
        self._wrapped_saver.save_data(data)

        # 2. Отправляем письмо
        self._mail_sender.send("admin@example.com")

        # 3. Обновляем кэш
        self._cache_updater.update_cache()


class DatabaseSaverClient:
    def main(self, b: bool) -> None:
        # Создаем экземпляры необходимых сервисов
        database_saver = DatabaseSaver()
        mail_sender = MailSender()
        cache_updater = CacheUpdater()

        # Оборачиваем DatabaseSaver в декоратор
        decorated_saver = DatabaseSaverDecorator(database_saver, mail_sender, cache_updater)

        # Используем декорированный объект
        self._do_smth(decorated_saver)

    def _do_smth(self, saver: IDatabaseSaver) -> None:
        saver.save_data(None)