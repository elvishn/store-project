from store_mq.database import mq_engine, create_tables  # Импорт из модуля store_mq


def test_connection():
    try:
        # Проверка подключения
        with mq_engine.connect() as conn:
            print("✅ Подключение к SQLite успешно!")
            print(f"Файл БД: {mq_engine.url.database}")

        # Создание таблиц
        create_tables()  # Теперь функция называется правильно
        print("Таблицы созданы!")

    except Exception as e:
        print(f"❌ Ошибка: {e}")


if __name__ == "__main__":
    test_connection()

