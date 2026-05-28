"""Homework scaffold — sqlite lesson `l2_types_and_affinity` (Vibe Learn).

Задача: аудит и нормализация типов: classify через typeof(?), audit_column, find_dirty, migrate_to_strict.

Реализуй функции ниже — сигнатуры и тестовая поверхность фиксированы;
CI (.github/workflows/ci.yml) ставит зависимости и гоняет `pytest`.
Подробности и критерии приёмки — в README.md.

SQLite встроена в Python через stdlib `sqlite3` — никакого драйвера ставить
не нужно, сервера нет. БД это файл (DATABASE_PATH) или ":memory:" в тестах.
"""

import os
import sqlite3


def database_path() -> str:
    """Путь к файлу БД из env. Дефолт ":memory:" — БД живёт в процессе."""
    return os.environ.get("DATABASE_PATH", ":memory:")


def connect(path: str | None = None) -> sqlite3.Connection:
    """Открыть соединение sqlite3 (по умолчанию из database_path())."""
    return sqlite3.connect(path if path is not None else database_path())


# ----- TODO #1: classify -----
def classify(value) -> str:
    """вернуть storage class значения через SELECT typeof(?) (null/integer/real/text/blob)"""
    raise NotImplementedError("classify: реализуй меня")


# ----- TODO #2: audit_column -----
def audit_column(conn, table: str, col: str) -> dict[str, int]:
    """{storage_class: count} по реальным классам значений в колонке"""
    raise NotImplementedError("audit_column: реализуй меня")


# ----- TODO #3: find_dirty -----
def find_dirty(conn, table: str, col: str, expected: set[str]) -> list:
    """строки, где typeof не входит в ожидаемый набор классов"""
    raise NotImplementedError("find_dirty: реализуй меня")


# ----- TODO #4: migrate_to_strict -----
def migrate_to_strict(conn, table: str, schema: str) -> None:
    """создать новую STRICT-таблицу, перенести данные с CAST, подменить старую"""
    raise NotImplementedError("migrate_to_strict: реализуй меня")



def main() -> None:
    """Точка входа: подключиться и напомнить, что реализовать.

    Замени тело на демонстрацию реализованных функций.
    """
    print("Vibe Learn — sqlite lesson scaffold up")
    print(f"DATABASE_PATH: {database_path()} (stdlib sqlite3, no server)")
    print("Реализуй TODO-функции, затем `pytest`. README.md содержит задачу.")


if __name__ == "__main__":
    main()
