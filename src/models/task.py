from dataclasses import dataclass


@dataclass
class Task:
    """Модель задачи.

    Содержит минимально необходимые поля: id и payload.
    """

    id: str
    payload: dict[str, object]
