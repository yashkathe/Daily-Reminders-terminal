# Step 1: Delete old broken venv
rm -rf bin lib lib64 pyvenv.cfg

# Step 2: Create new clean venv
python3 -m venv .

# Step 3: Activate it
source bin/activate

# Step 4: Confirm correct paths
which python
which pip
