import unittest

from src.contracts.source_protocol import TaskSource
from src.models.task import Task


class DummySource:
    """Простой источник для проверки контракта."""

    def get_tasks(self) -> list[Task]:
        """Вернуть одну тестовую задачу.

        :return: список из одной задачи
        """
        return [Task(id="dummy", payload={})]


class TestContracts(unittest.TestCase):
    """Тесты для проверки контрактов источников задач."""

    def test_dummy_source_is_task_source(self):
        """Проверить, что DummySource удовлетворяет протоколу TaskSource."""
        source = DummySource()
        self.assertIsInstance(source, TaskSource)


if __name__ == "__main__":
    unittest.main()
