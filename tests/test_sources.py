import json
import tempfile
import unittest
from pathlib import Path

from src.models.task import Task
from src.sources.api_source import ApiStubTaskSource
from src.sources.file_source import FileTaskSource
from src.sources.generator_source import GeneratedTaskSource


class TestSources(unittest.TestCase):
    """Набор тестов для источников задач."""

    def test_generated_task_source_basic(self):
        """Проверить базовую генерацию задач."""
        source = GeneratedTaskSource(count=3)
        tasks = source.get_tasks()

        self.assertEqual(len(tasks), 3)
        self.assertIsInstance(tasks[0], Task)
        self.assertEqual(tasks[0].id, "generated-0")
        self.assertEqual(tasks[1].payload["number"], 1)

    def test_file_task_source_reads_tasks(self):
        """Проверить чтение задач из файла."""
        raw_tasks = [
            {"id": "1", "payload": {"value": 10}},
            {"id": "2", "payload": {"value": 20}},
        ]

        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / "tasks.jsonl"

            with open(file_path, "w", encoding="utf-8") as f:
                for obj in raw_tasks:
                    f.write(json.dumps(obj) + "\n")

            source = FileTaskSource(str(file_path))
            tasks = source.get_tasks()

        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].id, "1")
        self.assertEqual(tasks[0].payload["value"], 10)

    def test_api_stub_task_source_works(self):
        """Проверить получение задач из API-заглушки."""

        def fake_api():
            return [
                {"id": "api-1", "payload": {"ok": True}},
                {"id": "api-2", "payload": {"ok": False}},
            ]

        source = ApiStubTaskSource(fetch_func=fake_api)
        tasks = source.get_tasks()

        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].id, "api-1")
        self.assertTrue(tasks[0].payload["ok"])

    def test_generator_negative_count(self):
        """Проверить, что отрицательное count вызывает ошибку."""
        with self.assertRaises(ValueError):
            GeneratedTaskSource(count=-1)

    def test_file_not_found(self):
        """Проверить ошибку при отсутствии файла."""
        source = FileTaskSource("non_existent_file.jsonl")
        with self.assertRaises(IOError):
            source.get_tasks()

    def test_file_invalid_json(self):
        """Проверить ошибку при неверном формате JSON."""
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / "invalid.jsonl"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("не json строка\n")

            source = FileTaskSource(str(file_path))
            with self.assertRaises(json.JSONDecodeError):
                source.get_tasks()


if __name__ == "__main__":
    unittest.main()
