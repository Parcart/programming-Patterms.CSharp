from Python.Ex05.ExternalLibs import DatabaseSaver, IDatabaseSaver


class DatabaseSaverClient:
    def main(self, b: bool) -> None:
        """
        Основной метод, аналогичный Main в C#
        Args:
            b: Булевый параметр (сохранен для соответствия сигнатуре, но не используется)
        """
        database_saver = DatabaseSaver()
        self._do_smth(database_saver)

    def _do_smth(self, saver: IDatabaseSaver) -> None:
        """
        Приватный метод, работающий через интерфейс
        Args:
            saver: Объект, реализующий интерфейс IDatabaseSaver
        """
        saver.save_data(None)