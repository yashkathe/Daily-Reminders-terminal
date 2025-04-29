import argparse

import questionary

from src.arg_options import list_options
from src.database import add_task, del_task, init_database, list_tasks
from src.greetings import print_instructions, print_snake
from src.user_inputs import get_user_inputs


def add_reminder():

    # greetings
    print_snake()
    print_instructions()

    # get user input & add task
    task_name, task_time, _, repeat_type = get_user_inputs()
    add_task(task_name, task_time, repeat_type)
    print(f"'{task_name}' added successfully!")


def unpack_reminders():

    tasks = list_tasks()

    # list tasks
    for i, [task, time, _] in enumerate(tasks):
        print(f"{i + 1} => {task} @ {time}")


def delete_reminder():

    tasks = list_tasks()

    # list out all the options
    choices = questionary.checkbox(
        "Select a Reminder to Delete:",
        choices=[f"{task} @ {time}" for task, time, _ in tasks],
    ).ask()

    # delete tasks from db
    for choice in choices:
        choice = choice.split("@")
        name, time = choice[0].strip(), choice[1].strip()
        del_task(name, time)
        print(f"{name} @ {time} deleted successfully")
    

if __name__ == "__main__":

    # setup argparse
    parser = argparse.ArgumentParser(
        description="A Lightweight Linux tool that lets you schedule reminders directly from the terminal, with notifications managed automatically in the background."
    )
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--add_reminder", action="store_true")
    parser.add_argument("--del_reminder", action="store_true")

    args = parser.parse_args()

    # init database
    init_database()

    # driver code
    if args.list:
        unpack_reminders()
    elif args.del_reminder:
        delete_reminder()
    elif args.add_reminder or not any(vars(args).values()):
        add_reminder()
    else:
        list_options(err=True)
