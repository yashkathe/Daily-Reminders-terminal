import questionary

choice = questionary.select(
    "Choose an option:",
    choices=["Option 1", "Option 2", "Option 3"]
).ask()

print(f"You chose: {choice}")
