#!/bin/bash

sudo service apache2 stop

source ~/env/bin/activate
cd ~/BackHackaZenvia/BackEnd
sudo find ./ -name "__pycache__" -type d -exec rm -rf {} +
git pull
git push

export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

pip install -r ~/BackHackaZenvia/BackEnd/requirements2

if [ $# -eq 1 ]; then
	clear
	echo ""
	echo "******************************************"
	while true; do
		read -p "Deletar DB? " yn
		case $yn in
			[Yy]* ) sudo rm -fr ~/BackHackaZenvia/BackEnd/app/app.db;  sudo rm -fr ~/BackHackaZenvia/BackEnd/migrations; break;;
			[Nn]* ) break;;
			* ) echo "Please answer yes or no.";;
		esac
	done
	echo "******************************************"
fi


flask db init
flask db migrate
flask db upgrade

sudo chown elder:www-data /home/elder/BackHackaZenvia/BackEnd/app/app.db
chmod 664 /home/elder/BackHackaZenvia/BackEnd/app/app.db

sudo service apache2 restart
sudo service apache2 reload
sudo find ./ -name "__pycache__" -type d -exec rm -rf {} +

