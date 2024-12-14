

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
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
- Post install (so that you don't need sudo):
```
sudo groupadd docker
sudo usermod -aG docker $USER
```
echo LOGOUT!!!