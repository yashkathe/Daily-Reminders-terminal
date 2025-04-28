import argparse

from database import add_task, init_database, list_tasks

from arg_options import list_options
from greetings import print_instructions, print_snake
from user_inputs import get_user_inputs


def add_reminder():

    # greetings
    print_snake()
    print_instructions()

    # get user input & add task
    task_name, task_time, _, repeat_type = get_user_inputs()
    add_task(task_name, task_time, repeat_type)
    print(f"'{task_name}' added successfully!")


if __name__ == "__main__":

    # setup argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--add_reminder", action="store_true")

    args = parser.parse_args()

    # Init database
    init_database()

    if args.list:
        list_tasks()
    elif args.add_reminder or not any(vars(args).values()):
        add_reminder()
    else:
        list_options(err=True)
