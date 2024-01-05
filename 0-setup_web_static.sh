#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

if [ ! -x /usr/sbin/nginx ]
then
	sudo apt-get -y update
	sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    <h1>Testing Nginx configuration <h1>
  </body>
</html>" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo chmod -R 755 /data/
sudo sed -i '48 i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart nginx
sudo service nginx restart
