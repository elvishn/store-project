import sys
import os
from pathlib import Path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.append(str(project_root))
from src.order_service.models.database import get_db
def test_product_table():
    conn = get_db()
    cursor = conn.cursor()

    print("\n=== Проверка таблицы product ===")

    # 1. Проверяем существование таблицы
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='product'")
    assert cursor.fetchone() is not None, "Таблица product не существует"
    print("✓ Таблица product существует")

    # 2. Проверяем структуру колонок
    cursor.execute("PRAGMA table_info(product)")
    columns = {row[1]: row[2] for row in cursor.fetchall()}
    expected_columns = {'id': 'TEXT', 'order_id': 'TEXT'}
    assert columns == expected_columns, f"Ожидались колонки: {expected_columns}, получено: {columns}"
    print("✓ Структура колонок корректна")

    # 3. Проверяем первичный ключ
    cursor.execute("SELECT pk FROM pragma_table_info('product') WHERE name = 'id'")
    assert cursor.fetchone()[0] == 1, "Поле id должно быть PRIMARY KEY"
    print("✓ Первичный ключ установлен")

    # 4. Проверяем FOREIGN KEY
    cursor.execute("PRAGMA foreign_key_list(product)")
    fk_info = cursor.fetchall()

    assert len(fk_info) > 0, "Не найдено ограничений FOREIGN KEY"
    print("\nИнформация о FOREIGN KEY:")
    for fk in fk_info:
        print(f"id: {fk[0]}, таблица: {fk[2]}, from: {fk[3]} → to: {fk[4]}")

    # Правильные индексы для SQLite:
    assert fk_info[0][2] == 'orders', f"Связь должна вести к 'orders', а не к '{fk_info[0][2]}'"
    assert fk_info[0][3] == 'order_id', f"Неправильное исходное поле: {fk_info[0][3]}"
    assert fk_info[0][4] == 'id', f"Связь должна быть с полем 'id', а не с '{fk_info[0][4]}'"
    print("✓ FOREIGN KEY корректна")

    conn.close()
    print("\nВсе проверки пройдены успешно!")


if __name__ == "__main__":
    test_product_table()