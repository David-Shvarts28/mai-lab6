## Лабораторная работа №1: источники задач и контракты

Платформа приёма задач.

- Домашняя модель задачи описана классом `Task`.
- Единый контракт источника задач задан через `typing.Protocol`.
- Разные источники (`FileTaskSource`, `GeneratedTaskSource`, `ApiStubTaskSource`) реализуют метод `get_tasks` без базового класса.

### Запуск приложения

```bash
python -m src.main
```

### Запуск тестов (unittest)

```bash
python -m unittest
```
