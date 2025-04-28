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
	$(PYTHON) $(MAIN)

add:
	@echo "➕ Adding a new reminder..."
	$(PYTHON) $(MAIN) --add_reminder

list:
	@echo "📋 Listing all reminders..."
	$(PYTHON) $(MAIN) --list

enable_service:
	@echo "🛠 Setting up systemd service..."
	@sudo bash -c 'cat > /etc/systemd/system/task_notifier.service' <<EOF
[Unit]
Description=Task Notifier Daemon
After=network.target

[Service]
ExecStart=/usr/bin/python3 $(shell pwd)/$(DAEMON)
Restart=always
User=$(shell whoami)
WorkingDirectory=$(shell pwd)
StandardOutput=inherit
StandardError=inherit

[Install]
WantedBy=multi-user.target
EOF
	sudo systemctl daemon-reload
	sudo systemctl enable task_notifier
	sudo systemctl start task_notifier
	@echo "✅ Service enabled and started."

disable_service:
	@echo "🛑 Stopping and disabling service..."
	@sudo systemctl stop task_notifier
	@sudo systemctl disable task_notifier
	@sudo rm -f /etc/systemd/system/task_notifier.service
	@sudo systemctl daemon-reload
	@echo "✅ Service disabled."

status_service:
	@sudo systemctl status task_notifier

restart_service:
	@sudo systemctl restart task_notifier
