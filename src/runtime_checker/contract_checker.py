from src.contracts.source_protocol import TaskSource


def check_isinstance(source) -> TaskSource:
    """Проверить, что объект удовлетворяет контракту TaskSource.

    :param source: произвольный объект для проверки на источник задач.
    :return: тот же объект, прошедший проверку.
    :raises TypeError: исключение, если объект не является источником задач.
    """
    if not isinstance(source, TaskSource):
        raise TypeError("Объект не является источником задач")
    return source
