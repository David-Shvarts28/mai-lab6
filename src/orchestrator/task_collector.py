from src.contracts.source_protocol import TaskSource
from src.models.task import Task
from src.runtime_checker.contract_checker import check_isinstance


class TaskCollector:
    """Сборщик задач из источников."""

    def __init__(self) -> None:
        self._sources: list[TaskSource] = []

    def add_source(self, source: object) -> None:
        """Добавить источник в коллекцию.

        :param source: любой объект, который должен удовлетворять контракту TaskSource.
        """
        check_isinstance(source)
        self._sources.append(source) #type: ignore

    def collect_tasks(self) -> list[Task]:
        """Собрать задачи из всех источников.

        :return: список Task, полученных из всех источников.
        """
        tasks: list[Task] = []
        for source in self._sources:
            tasks.extend(source.get_tasks())
        return tasks
