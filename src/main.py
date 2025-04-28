import argparse
import schedule
import time

from greetings import print_snake, print_instructions
from arg_options import list_options
from user_inputs import get_user_inputs
from schedule_notify import schedule_reminder
from database import add_task, list_tasks, init_database 

def main():
    
    # greet
    print_snake()
    print_instructions()

    # init 
    init_database()

    # schedule existing tasks
    for task_name, task_time, repeat_type in list_tasks():
        schedule_reminder(task_name, task_time, repeat_type)
    
    # get, save & schedule user input 
    task_name, task_time, _, repeat_type = get_user_inputs()
    add_task(task_name, task_time, repeat_type)
    schedule_reminder(task_name, task_time, repeat_type)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--add_reminder', action='store_true')

    args = parser.parse_args()

    if args.list:
        list_tasks()
    elif args.add_reminder or not any(vars(args).values()):
        main()
    else:        
        list_options(err=True)
