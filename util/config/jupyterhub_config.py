from traitlets.config import get_config
from jupyterhub.auth import DummyAuthenticator
import os

c = get_config()

# Authentication settings - put these first!
c.JupyterHub.authenticator_class = DummyAuthenticator
c.DummyAuthenticator.password = "test123"
c.Authenticator.admin_users = {'yuval'}
c.Authenticator.allowed_users = {'yuval'}

# Remove this line as it's for LocalAuthenticator
# c.LocalAuthenticator.create_system_users = True

# Basic Configuration
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000

# Use DockerSpawner
# c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.JupyterHub.spawner_class = "simple"

c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
c.DockerSpawner.network_name = 'jupyterhub-network'
c.DockerSpawner.remove = True

# Debug and security
c.JupyterHub.log_level = 'DEBUG'
c.JupyterHub.cookie_secret = bytes(32)
c.ConfigurableHTTPProxy.auth_token = bytes(32)