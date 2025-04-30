import time

import schedule

from src.database import init_database, list_tasks
from src.schedule_notify import schedule_reminder


def main():
    init_database()
    scheduled_set = set()

    while True:
        for task_name, task_time, repeat_type in list_tasks():
            key = (task_name, task_time, repeat_type)
            if key not in scheduled_set:
                schedule_reminder(task_name, task_time, repeat_type)
                scheduled_set.add(key)

        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
