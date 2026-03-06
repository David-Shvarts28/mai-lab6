from src.models.task import Task


class ApiStubTaskSource:
    """Источник задач из API-заглушки."""

    def __init__(self, fetch_func) -> None:
        """Создать источник с функцией-заглушкой.

        :param fetch_func: функция, возвращающая список словарей с задачами
        """
        self._fetch_func = fetch_func

    def get_tasks(self) -> list[Task]:
        """Получить задачи из API-заглушки.

        :return: список объектов Task, построенных по данным из заглушки.
        """
        raw_data = self._fetch_func()
        tasks = []
        for item in raw_data:
            task_id = str(item["id"])
            payload = item.get("payload", {})
            tasks.append(Task(id=task_id, payload=payload))
        return tasks
