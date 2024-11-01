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

vim backend/app/controllers/conection.py

sudo docker compose up -d

## Proxy reverso e Load Balance

sudo apt update

sudo apt install nginx - y

git --version

git clone https://github.com/KhovetS2/projeto-redes.git

sudo cp proxy/loadbalance.conf /etc/nginx/conf.d/

sudo rm /etc/nginx/sites-available/default 

sudo cp proxy/default /etc/nginx/sites-available/

sudo nginx -t

sudo nginx -s reload
