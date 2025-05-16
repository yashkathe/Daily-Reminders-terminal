import time

import schedule

from src.database import init_database, list_tasks
from src.schedule_notify import schedule_reminder


def main():
    init_database()
    scheduled_jobs = {}

    while True:
        current_tasks = set()

        for task_name, task_time, repeat_type in list_tasks():
            key = (task_name, task_time, repeat_type)
            current_tasks.add(key)

            if key not in scheduled_jobs:
                job = schedule_reminder(task_name, task_time, repeat_type)
                if job:
                    scheduled_jobs[key] = job

        # Unschedule tasks removed from DB
        for key in list(scheduled_jobs):
            if key not in current_tasks:
                schedule.cancel_job(scheduled_jobs[key])
                del scheduled_jobs[key]

        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
