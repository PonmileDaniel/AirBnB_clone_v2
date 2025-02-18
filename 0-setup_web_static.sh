#!/usr/bin/env bash
# Script to set up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
nginx_conf="server {
    listen 80;
    server_name localhost;

    location /hbnb_static {
        alias /data/web_static/current;
    }
}"
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.backup
echo "$nginx_conf" | sudo tee /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
