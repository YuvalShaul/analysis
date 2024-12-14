

### Preparations

- Install git:
```
sudo apt-get update
sudo apt install git-all
```
- Clone the analysis repository:
```
git clone https://github.com/YuvalShaul/analysis.git
```
- Install docker:
```
source install_docker_ubuntu
```

## Conf

- exec into the container:
```
docker exec -it jupyterhub bash
```
- Create a new system user:
```
adduser yuval
```
- Restart compose:
```
docker compose restart jupyterhub
```