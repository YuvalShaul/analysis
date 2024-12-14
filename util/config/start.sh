#!/bin/bash

# Function to generate random password
generate_password() {
    tr -dc 'A-Za-z0-9!@#$%^&*' < /dev/urandom | head -c 12
}

# Generate random passwords
PASS_DAVE=$(generate_password)
PASS_JOHN=$(generate_password)

# Create users if they don't exist
useradd -m -s /bin/bash dave || echo "User dave already exists"
useradd -m -s /bin/bash john || echo "User john already exists"

# Set passwords
echo "dave:$PASS_DAVE" | chpasswd
echo "john:$PASS_JOHN" | chpasswd

# Print the credentials (they will appear in docker logs)
echo "=========================="
echo "Generated credentials:"
echo "User: dave  Password: $PASS_DAVE"
echo "User: john   Password: $PASS_JOHN"
echo "=========================="

# Start JupyterHub
jupyterhub -f /etc/jupyterhub/jupyterhub_config.py