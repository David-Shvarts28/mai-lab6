## Лабораторная работа №1: источники задач и контракты

Простейшая платформа приёма задач для учебных целей.

- Домашняя модель задачи описана классом `Task` (модуль `task_model`).
- Единый контракт источника задач задан через `typing.Protocol` (`TaskSource` в модуле `contracts`).
- Разные источники (`FileTaskSource`, `GeneratedTaskSource`, `ApiStubTaskSource`) реализуют метод `get_tasks` без общего базового класса.

### Запуск приложения

```bash
python -m src.main
```

### Запуск тестов (unittest)

```bash
python -m unittest
```
