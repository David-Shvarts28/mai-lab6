from src.orchestrator.task_collector import TaskCollector
from src.sources.api_source import ApiStubTaskSource
from src.sources.generator_source import GeneratedTaskSource


def fake_api() -> list[dict]:
    """Имитация внешнего API, возвращающего список задач.

    :return: список словарей с полями id и payload.
    """
    return [
        {"id": "api-1", "payload": {"message": "hello"}},
        {"id": "api-2", "payload": {"message": "Peter"}},
        {"id": "api-3", "payload": {"message": "Zhabin"}}]


def main() -> None:
    """Точка входа в приложение."""
    collector = TaskCollector()

    generated_source = GeneratedTaskSource(count=3)
    api_source = ApiStubTaskSource(fetch_func=fake_api)

    collector.add_source(generated_source)
    collector.add_source(api_source)

    all_tasks = collector.collect_tasks()

    print("Полученные задачи:")
    for task in all_tasks:
        print(f"id={task.id!r}, payload={task.payload}")


if __name__ == "__main__":
    main()
