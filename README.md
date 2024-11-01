# projeto-redes

## Banco de dados
sudo apt update

git --version

git clone https://github.com/KhovetS2/projeto-redes.git

cd projeto-redes/

chmod +x script-docker.sh

./script-docker.sh

cd db/

sudo docker compose up -d

## Backend

sudo apt update

git --version

git clone https://github.com/KhovetS2/projeto-redes.git

cd projeto-redes/

chmod +x script-docker.sh

./script-docker.sh

vim backend/config.py

sudo docker compose up -d

## Proxy reverso e Load Balance

sudo apt update

sudo apt install nginx - y

git --version

git clone https://github.com/KhovetS2/projeto-redes.git

sudo cp projeto-redes/proxy.conf /etc/nginx/conf.d/
