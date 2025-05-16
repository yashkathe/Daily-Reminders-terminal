def list_options(err=False):

    if err:
        print("Not a Valid Argument")

    print(
        """
    Available Options
    \n
    no args = Run Normal Script to Set up a Reminder
    --list = List your scheduled reminders
    --help = List of all arguments
    """
    )
