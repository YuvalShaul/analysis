#!/bin/bash

# Create user if doesn't exist
useradd -m -s /bin/bash yuval || echo "User already exists"

# Start JupyterHub
jupyterhub -f /etc/jupyterhub/jupyterhub_config.py