class DatabaseSaverClient:
    def main(self, b: bool) -> None:
        database_saver = DatabaseSaver()
        self._do_smth(database_saver)

    def _do_smth(self, saver: IDatabaseSaver) -> None:
        saver.save_data(None)