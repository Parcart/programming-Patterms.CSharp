from abc import ABC, abstractmethod

# Этот код моделирует класс FtpClient, который нельзя менять в соответствии с условиями задания.
# В реальном проекте он, вероятно, будет частью внешней библиотеки.

class FtpClient:
    """
    Моделирует упрощенный FTP-клиент.
    Этот класс предназначен для примера и не содержит реальной функциональности FTP.
    """

    def read_file(self, login: str, password: str, file_path: str) -> str:
        """
        Читает файл с удаленного FTP-сервера.

        Args:
            login (str): Логин пользователя FTP.
            password (str): Пароль пользователя FTP.
            file_path (str): Путь к файлу на удаленном сервере.

        Returns:
            str: Содержимое файла (в данном случае пустая строка).
        """
        # В реальном коде здесь была бы логика подключения к FTP, аутентификации,
        # загрузки файла и возвращения его содержимого.  Но так как класс менять нельзя,
        # мы просто возвращаем пустую строку.
        return ""  # Заглушка: имитируем ситуацию, когда файл прочитан успешно (но ничего не содержит)


# Этот код моделирует класс FileLogReader, который нельзя изменять по условиям задания.
# Как и в C#, он имитирует внешний компонент или библиотеку.



class ILogReader(ABC): # Абстрактный базовый класс

    @abstractmethod
    def read_log_file(self, identificator: str) -> str:
        """
        Абстрактный метод для чтения лог-файла.

        Args:
            identificator (str): Идентификатор для поиска лог-файла (например, имя файла).

        Returns:
            str: Содержимое лог-файла.
        """
        pass  # Этот метод должен быть реализован в подклассах

class FileLogReader(ILogReader): # Класс, реализующий интерфейс ILogReader
    """
    Реализует чтение лог-файлов из файловой системы.
    По условиям задания, этот класс нельзя изменять.
    """

    def read_log_file(self, identificator: str) -> str:
        """
        Читает лог-файл по идентификатору (имени файла).

        Args:
            identificator (str): Идентификатор лог-файла (имя файла).

        Returns:
            str: Содержимое лог-файла (в данном случае всегда "FILE").
        """
        # В реальном коде здесь была бы логика поиска и чтения файла.
        # Но так как класс менять нельзя, мы просто возвращаем предопределенное значение.
        return "FILE" # Возвращаем всегда "FILE", как в C# коде


# Этот код имитирует класс LogImporter, который нельзя менять по условиям задания.
# Нужно расширить функциональность, не изменяя существующую.
class LogImporter:
    """
    Импортирует логи из различных источников, используя объект ILogReader.
    Нельзя изменять существующую функциональность, только расширять.
    """

    def __init__(self, reader: ILogReader):
        """
        Инициализирует объект LogImporter с помощью объекта ILogReader.

        Args:
            reader (ILogReader): Объект, реализующий интерфейс ILogReader.
        """
        self._reader = reader

    def import_logs(self, source: str):
        """
        Импортирует логи из указанного источника.

        Args:
            source (str): Идентификатор источника логов (например, имя файла).
        """
        file_content = self._reader.read_log_file(source)
        # Здесь должна быть логика обработки содержимого файла.
        # Сейчас это просто заглушка.
        print(f"Importing logs from {source} (content: {file_content})") # Заглушка для демонстрации работы
        # TODO: Добавьте логику обработки file_content

    def extended_import_logs(self, source: str, extra_param: str):  # Пример расширения функциональности
        """
        Расширенная версия импорта логов с дополнительным параметром.

        Args:
            source (str): Идентификатор источника логов.
            extra_param (str): Дополнительный параметр для расширенной обработки.
        """
        file_content = self._reader.read_log_file(source)
        # Здесь должна быть логика обработки содержимого файла с использованием extra_param.
        print(f"Importing logs from {source} with extra param {extra_param} (content: {file_content})")
        # TODO: Добавьте логику обработки file_content и extra_param


class LogImporterClient:
    """
    Клиентский класс, использующий LogImporter для импорта логов.
    Изменения вносятся только в метод do_method.
    """


    def do_method(self):
        """
        Выполняет импорт логов с использованием LogImporter и FileLogReader.
        """

        # 1. Создаем экземпляр FileLogReader (или другого ILogReader)
        file_log_reader = FileLogReader()

        # 2. Создаем экземпляр LogImporter, передавая ему объект ILogReader
        log_importer = LogImporter(file_log_reader)

        # 3. Вызываем метод ImportLogs для импорта логов
        log_importer.import_logs("ftp://log.txt")

        # Пример использования расширенной функциональности (если такая есть)
        # log_importer.extended_import_logs("ftp://log.txt", "debug") # Если определили extended_import_logs

        # TODO: Добавьте другую логику, используя log_importer и file_log_reader

# Пример использования класса LogImporterClient
if __name__ == "__main__":
    client = LogImporterClient()
    client.do_method()