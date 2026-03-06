import unittest

from src.contracts.source_protocol import TaskSource
from src.models.task import Task
from src.orchestrator.task_collector import TaskCollector
from src.sources.generator_source import GeneratedTaskSource


class CustomSource:
    """Пользовательский источник задач для тестов."""

    def __init__(self, ids):
        """Сохранить идентификаторы задач.

        :param ids: список идентификаторов
        """
        self._ids = ids

    def get_tasks(self) -> list[Task]:
        """Вернуть задачи с сохранёнными идентификаторами.

        :return: список задач
        """
        tasks = []
        for task_id in self._ids:
            tasks.append(Task(id=task_id, payload={"source": "custom"}))
        return tasks


class TestTaskCollector(unittest.TestCase):

    def test_collector_accepts_valid_sources(self):
        """Проверить, что коллектор принимает корректные источники."""
        collector = TaskCollector()

        gen_source = GeneratedTaskSource(count=2)
        custom_source = CustomSource(ids=["a", "b"])

        collector.add_source(gen_source)
        collector.add_source(custom_source)

        tasks = collector.collect_tasks()
        self.assertEqual(len(tasks), 4)

        ids = [t.id for t in tasks]
        self.assertIn("generated-0", ids)
        self.assertIn("generated-1", ids)
        self.assertIn("a", ids)
        self.assertIn("b", ids)

    def test_collector_rejects_invalid_source(self):
        """Проверить, что коллектор отклоняет некорректный источник."""
        collector = TaskCollector()

        class NotASource:
            pass

        bad_source = NotASource()

        with self.assertRaises(TypeError):
            collector.add_source(bad_source)

    def test_custom_source_is_instance_of_protocol(self):
        """Проверить, что CustomSource удовлетворяет протоколу TaskSource."""
        custom = CustomSource(ids=["x"])
        self.assertIsInstance(custom, TaskSource)


if __name__ == "__main__":
    unittest.main()
