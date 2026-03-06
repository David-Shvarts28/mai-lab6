from typing import Protocol, runtime_checkable

from src.models.task import Task


@runtime_checkable
class TaskSource(Protocol):
    """Контракт источника задач.

    Источники задач должны реализовывать этот протокол.
    Проверка контракта выполняется через isinstance() в рантайме.
    """

    def get_tasks(self) -> list[Task]:
        """Функция, возвращающая список задач из источника.

        :return: список объектов Task, полученных из источника.
        :raises Exception: ошибка при чтении.
        """
        pass
