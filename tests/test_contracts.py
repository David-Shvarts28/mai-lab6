import unittest

from src.contracts.source_protocol import TaskSource
from src.models.task import Task


class DSource:
    """Источник для проверки контракта."""

    def get_tasks(self) -> list[Task]:
        """Вернуть одну тестовую задачу.

        :return: список из одной задачи
        """
        return [Task(id="d", payload={})]


class TestContracts(unittest.TestCase):
    """Тесты для проверки контрактов источников задач."""

    def test_d_source_task(self):
        """DSource удовлетворяет протоколу TaskSource."""
        source = DSource()
        self.assertIsInstance(source, TaskSource)


if __name__ == "__main__":
    unittest.main()
