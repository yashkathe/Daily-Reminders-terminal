.PHONY: install run add list enable_service disable_service status_service restart_service

# Path to your daemon and main scripts
DAEMON=src/scripts/daemon.py
MAIN=src/main.py

# Python interpreter
PYTHON=python3

install:
	@echo "🔧 Installing dependencies..."
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt
	@echo "✅ Dependencies installed."

run:
	@echo "🚀 Running program (add task)..."
	$(PYTHON) -m src.main

add:
	@echo "➕ Adding a new reminder..."
	$(PYTHON) -m src.main --add_reminder

list:
	@echo "📋 Listing all reminders..."
	$(PYTHON) -m src.main --list

enable_service:
	@echo "🛠 Setting up user systemd service..."
	@mkdir -p ~/.config/systemd/user
	@sed "s|/REPO_PATH|$(shell pwd)|g" src/scripts/task_notifier.service | \
	sed "s|USERNAME|$(shell whoami)|g" | \
	tee ~/.config/systemd/user/task_notifier.service > /dev/null
	systemctl --user daemon-reload
	systemctl --user enable task_notifier
	systemctl --user start task_notifier
	@echo "✅ User service enabled and started."

disable_service:
	@echo "🛑 Stopping and disabling user service..."
	systemctl --user stop task_notifier
	systemctl --user disable task_notifier
	@rm -f ~/.config/systemd/user/task_notifier.service
	systemctl --user daemon-reload
	@echo "✅ User service disabled."

status_service:
	systemctl --user status task_notifier

restart_service:
	systemctl --user restart task_notifier
