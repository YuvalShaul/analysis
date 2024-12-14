#!/bin/bash

# Create users if they don't exist (needed for LocalProcessSpawner)
useradd -m -s /bin/bash yuval || echo "User yuval already exists"
useradd -m -s /bin/bash john || echo "User john already exists"

# Print the credentials
echo "=========================="
echo "Credentials:"
echo "User: yuval  Password: pass_yuval"
echo "User: john   Password: pass_john"
echo "=========================="

# Start JupyterHub
jupyterhub -f /etc/jupyterhub/jupyterhub_config.py