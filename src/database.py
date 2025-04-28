import os
import sqlite3
from sqlite3.dbapi2 import connect

DB_FILE = "tasks.db"


# create sqlite table if it doesn't exist
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
        """
        )
        conn.commit()
        conn.close()

    except Exception as e:
        print(e)
        return 1

    return 0


# add data to sqlite table
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
        print(e)
        return 1


# list all tasks
def list_tasks():

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            """
        SELECT name, time, repeat_type FROM tasks
        """
        )

    except Exception as e:
        print(e)
        return 1

    return 1
