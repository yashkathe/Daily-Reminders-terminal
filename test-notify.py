# import notify2

# # Initialize the notification library
# notify2.init("Notification Example")

# # Create a notification object
# notification = notify2.Notification(
#     "Hello from Python!",  # Title
#     "This is a GNOME notification triggered using Python.",  # Message
#     "dialog-information"  # Icon (can be None for default)
# )

# # Set urgency level (optional)
# notification.set_urgency(notify2.URGENCY_NORMAL)

# # Set timeout for the notification (in milliseconds)
# notification.set_timeout(5000)

# # Show the notification
# notification.show()

import notify2
notify2.init('Test')
n = notify2.Notification("Test Title", "Test Body")
n.show()
