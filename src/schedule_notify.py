from datetime import datetime

import notify2
import schedule

from src.util.error_fn import error_and_exit


def init_notify2():
    notify2.init("User Reminder")


init_notify2()


def send_notification(task_name):
    try:
        print(f"Reminder: {task_name}")
        notification = notify2.Notification("Task Reminder", f"Time to: {task_name}")
        notification.set_urgency(notify2.URGENCY_NORMAL)
        notification.set_timeout(5000)
        notification.show()
    except Exception as e:
        print(f"Notification error: {e}")


def schedule_reminder(task_name, task_time, repeat_type):
    def job():
        print(f"Running task: {task_name} at {datetime.now().strftime('%H:%M:%S')}")
        send_notification(task_name)

    try:
        if repeat_type == "h":
            minutes = task_time[-2:]
            return schedule.every().hour.at(f":{minutes}").do(job)
        elif repeat_type == "d":
            return schedule.every().day.at(task_time).do(job)
        else:
            return schedule.every().day.at(task_time).do(job)
    except Exception as e:
        error_and_exit(e)
