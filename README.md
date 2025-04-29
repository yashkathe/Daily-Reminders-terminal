# Set Reminders Terminal


## Install and Setup

1. Clone the project or download it.

2. Install required Python packages using:

   ```bash
   make install
   ```

   _This will install all needed libraries from `requirements.txt`._

3. Enable and start the background service:

   ```bash
   make enable_service
   ```

   _This will create a system service that runs the reminder program silently in the background._

---

## Add a new reminder

```bash
make add
```

_This will open a simple prompt. You can enter your task and time._

---

## List all reminders

```bash
make list
```

_This will show you all the saved tasks from the database._

---

## Service Controls

- Check if the service is running:

  ```bash
  make status_service
  ```

- Restart the service manually:

  ```bash
  make restart_service
  ```

- Stop and disable the service (remove from startup):

  ```bash
  make disable_service
  ```

## Troubleshoot

- Service is not running:

    ```bash
    sudo journalctl -u task_notifier -e | tail
    ```

_Check the logs_  

---

# How it works

- The program saves your tasks into a small database (SQLite file).
- A small hidden program (daemon.py) keeps checking the tasks in background.
- It sends you a notification at the right time.
- You can add new reminders anytime with a simple command.
- The service will auto-start after your computer reboots.

---

# Quick Start

```bash
make install
make enable_service
make add
make list
```
