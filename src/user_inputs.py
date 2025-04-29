import time 
import re
from datetime import datetime

from src.util.error_fn import error_and_exit

def get_user_inputs():

    # reminder's name
    reminder_name = input('Remind me that?\n').strip().lower()

    # repeat or not
    repeat = input('Should the Task be Repeated (y/n) \n').strip().lower()

    if repeat != 'y' and repeat != 'n':
        error_and_exit('Not a Valid Input - select: y or n')

    # time to remind
    time_raw = input('At Time (HH:MM) in 24 hour format\n').strip()

    valid_time = r"^(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])$"

    if not re.match(valid_time, time_raw) :
        error_and_exit('Invalid Format for Time - eg: 12:30')

    time = datetime.strptime(time_raw, "%H:%M").strftime("%H:%M")

    # remind every hour or day
    repeat_type = None
    if repeat == 'y':
        repeat_type = input('Repeat every hour (\'h\') or every day (\'d\') ')

    if repeat_type and repeat_type != 'h' and repeat_type != 'd':
        error_and_exit('Not a Valid Input - select: h or d')

    return reminder_name, time, repeat, repeat_type
