import sqlite3

from src.util.error_fn import error_and_exit

DB_FILE = "tasks.db"


def init_database():

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                time TEXT NOT NULL,
                repeat_type TEXT
            )
        """
        )
        conn.commit()
        conn.close()

    except Exception as e:
        error_and_exit(f"database error: {e}")


def add_task(name, time, repeat_type):

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO tasks (name, time, repeat_type)
            VALUES (?, ?, ?)
        """,
            (name, time, repeat_type),
        )
        conn.commit()
        conn.close()

    except Exception as e:
        error_and_exit(f"database error: {e}")


def del_task(name, time):

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM tasks
            WHERE name = ? AND time = ?
            """,
            (name, time),
        )
        conn.commit()
        conn.close()

    except Exception as e:
        error_and_exit(f"database error: {e}")


def list_tasks():

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT name, time, repeat_type FROM tasks")
        tasks = cursor.fetchall()
        conn.close()
        return tasks

    except Exception as e:
        error_and_exit(f"database error: {e}")
