import asyncio
from typing import List, Callable, Coroutine, Any

from Python.Ex05.ExternalLibs import DatabaseSaver, IDatabaseSaver, MailSender, CacheUpdater


class AsyncDatabaseExecutor(IDatabaseSaver):
    def __init__(self, saver: IDatabaseSaver):
        self._saver = saver
        self._tasks: List[Coroutine[Any, Any, None]] = []

    def add_operation(self, coro_func: Coroutine[Any, Any, None]):
        self._tasks.append(coro_func)

    async def save_data(self, data: object) -> None:
        # Основное сохранение
        await self._saver.save_data(data)

        # Запуск всех операций конкурентно. p.s. в таску оборачивать не обязательно, зависит от пожеланий)
        tasks = [asyncio.create_task(task) for task in self._tasks]
        await asyncio.gather(*tasks)


# Обертки для синхронных операций
async def send_mail():
    # Переносим синхронный вызов в отдельный поток
    await asyncio.to_thread(MailSender().send, "admin@example.com")


async def update_cache():
    await asyncio.to_thread(CacheUpdater().update_cache)


# Клиентский код
class AsyncDatabaseSaverClient:
    async def main(self, b: bool) -> None:
        # Инициализация
        executor = AsyncDatabaseExecutor(DatabaseSaver())

        # Добавляем операции как корутины
        coro = send_mail()
        executor.add_operation(coro)
        executor.add_operation(update_cache())

        # Добавить новую операцию можно просто:
        # executor.add_operation(some_async_fn(params))

        await self._do_smth(executor)

    async def _do_smth(self, saver: IDatabaseSaver) -> None:
        saver.save_data(None)


# асинхронность, ну использовать lamba для обертки и передачи операции в синхронном коде, ну это кринге, ну как по мне, ну можно и многопоточную реализую сделать, но асинхронность круче
# Да и в целом даже ансинхронно не самая лучшая реализация, я спать.
