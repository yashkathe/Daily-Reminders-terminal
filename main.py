import argparse

from greetings import print_snake, print_instructions
from prompt_user import get_user_inputs
from arg_options import list_options

def main():
    print_snake()
    print_instructions()
    get_user_inputs()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--add_reminder', action='store_true')

    args = parser.parse_args()

    if args.list:
        list_options()
    elif args.add_reminder or not any(vars(args)):
        main()
    else:        
        list_options(err=True)
