import schedule
import time

from database import init_database, list_tasks
from schedule_notify import schedule_reminder

def main():
    
    # init database
    init_database()

    # load all saved tasks & schedule them
    for task_name, task_time, repeat_type in list_tasks():
        schedule_reminder(task_name, task_time, repeat_type)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
