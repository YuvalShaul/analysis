from traitlets.config import get_config
import os

c = get_config()

# Basic Configuration
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000

# Use DockerSpawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# Specify container image
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']

# Connect containers to the custom Docker network
c.DockerSpawner.network_name = 'jupyterhub-network'

# Remove containers when they're shut down
c.DockerSpawner.remove = True

# For debugging
c.JupyterHub.log_level = 'DEBUG'

# Use Local Authenticator
c.JupyterHub.authenticator_class = 'jupyterhub.auth.LocalAuthenticator'

c.Authenticator.admin_users = {'yuval'}

c.JupyterHub.authenticator_class = 'jupyterhub.auth.LocalAuthenticator'
c.LocalAuthenticator.create_system_users = True