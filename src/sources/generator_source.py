from src.models.task import Task


class GeneratedTaskSource:
    """Источник задач, который генерирует задачи программно.

    Создает задачи с идентификаторами вида generated-0, generated-1 и т.д.
    """

    def __init__(self, count: int) -> None:
        """Создать источник с указанным количеством задач.

        :param count: количество задач для генерации
        :raises ValueError: если count < 0
        """
        if count < 0:
            raise ValueError("Количество задач не может быть отрицательным")
        self._count = count

    def get_tasks(self) -> list[Task]: #type: ignore
        """Сгенерировать задачи.

        :return: список сгенерированных задач Task
        """
        tasks = []
        for i in range(self._count):
            task_id = f"generated-{i}"
            payload = {"number": i}
            tasks.append(Task(id=task_id, payload=payload)) #type: ignore
        return tasks
