# Notify Me

Notify Me is a lightweight Linux tool that lets you schedule daily or hourly reminders directly from the terminal, with notifications managed automatically in the background.

<div align="center">

<img src="./docs/reminders-logo.png" width="300">

</div>

<div align="center">

<img src="https://img.shields.io/badge/license-GPL_v3.0-blue.svg" alt="License">
<img src="https://img.shields.io/github/last-commit/yashkathe/Notify-Me-Terminal-App.svg" alt="Last Commit">
<img src="https://img.shields.io/badge/platform-linux-important" alt="Platform">
<img src="https://img.shields.io/github/repo-size/yashkathe/Notify-Me-Terminal-App.svg" alt="Repo Size">
<img src="https://img.shields.io/github/languages/top/yashkathe/Notify-Me-Terminal-App.svg" alt="Main Language">

</div>

## Install and Setup

1. Clone the project or download it.

    ```bash
    git clone https://github.com/yashkathe/Notify-Me-Terminal-App.git
    ```

2. Install required Python packages:

   ```bash
   make install
   ```

   *This will install all needed libraries from requirements.txt.*

3. Enable and start the background service:

   ```bash
   make enable_service
   ```

   *This will create a system service that runs the reminder program silently in the background.*

### Add a new reminder

```bash
make add
```

 *This will open a simple prompt. You can enter your task and time.*

### List all reminders

```bash
make list
```

 *This will show you all the saved tasks from the database.*

### Service Controls

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

### Troubleshoot

- check logs of daemon if its not working as expected

    ```bash
    sudo journalctl -u task_notifier -e | tail
    ```

## How it works

- The program saves your tasks into a small database (SQLite file).
- A script (daemon.py) keeps checking the tasks in background.
- It sends you a notification at the right time.
- You can add new reminders anytime with a simple command.
- The service auto-start and data is persisted after your computer reboots.

## Quick Start

```bash
make enable_service
make add
make list
```

---
