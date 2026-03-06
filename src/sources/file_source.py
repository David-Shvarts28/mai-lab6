import json

from src.models.task import Task


class FileTaskSource:
    """Источник задач, считывающий данные из файла.

    Каждая строка файла должна быть JSON с полями id и payload.
    """

    def __init__(self, path: str) -> None:
        """Создать источник с указанным файлом.

        :param path: путь к файлу с задачами
        """
        self._path = path

    def get_tasks(self) -> list[Task]:
        """Считать задачи из файла.

        :return: список задач Task
        :raises IOError: ошибка чтения файла
        """
        tasks = []
        with open(self._path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                data = json.loads(line)
                task_id = str(data["id"])
                payload = data.get("payload", {})
                tasks.append(Task(
                    id=task_id,
                    payload=payload
                ))
        return tasks
