ls
cd home
ls
dir
cd home
cd root
ls
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx
sudo -u postgres psql
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
mkdir ~/myproject
cd ~/myproject
virtualenv myprojectenv
source myprojectenv/bin/activate
pip install django gunicorn psycopg2
django-admin.py startproject myproject ~/myproject
nano ~/myproject/myproject/settings.py
source myprojectenv/bin/activate
cd ~/myproject
source myprojectenv/bin/activate
~/myproject/manage.py makemigrations
~/myproject/manage.py migrate
~/myproject/manage.py makemigrations
~/myproject/manage.py migrate
~/myproject/manage.py createsuperuser
~/myproject/manage.py collectstatic
sudo ufw allow 8000
~/myproject/manage.py runserver 0.0.0.0:8000
cd ~/myproject
gunicorn --bind 0.0.0.0:8000 myproject.wsgi
deactivate
sudo nano /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn
ls /home/sammy/myproject
sudo journalctl -u gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo nano /etc/nginx/sites-available/myproject
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo nginx -t
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo nano /etc/nginx/sites-available/myproject
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl restart gunicorn
sudo systemctl status postgresql
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo nginx -t && sudo systemctl restart nginx
sudo systemctl restart gunicorn
sudo nano /etc/nginx/sites-available/myproject
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo nginx -t
cd /et/nginx/sites-enabled/
cd /etc/nginx/
ls
sites-enabled
cd sites-enabled
ls
NANO MYPROJECT
nano myproject
nano defaut
nano default
cd ..
ls
cd sites-available/
ls
nano myproject 
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
cd ..
nano sites-enabled/
ls
cd sites-enabled/
ls
rm myproject 
sudo rm myproject 
cd ..
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
ls
sudo nginx -t
sudo systemctl restart nginx
systemctl status nginx.service
sudo nano /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn
sudo journalctl -u gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo nano /etc/nginx/sites-available/myproject
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo rm /etc/nginx/sites-enabled/myproject
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo nginx -t
sudo rm /etc/nginx/sites-enabled/myproject
sudo nano /etc/nginx/sites-available/myproject
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo nginx -t
sudo rm /etc/nginx/sites-enabled/myproject
sudo nano /etc/nginx/sites-available/myproject
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo nginx -t
systemctl status nginx.service
sudo rm /etc/nginx/sites-enabled/myproject
sudo nano /etc/nginx/sites-available/myproject
sudo nginx -t
sudo systemctl restart nginx
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'
sudo nano /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn
sudo journalctl -u gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo nano /etc/nginx/sites-available/myproject
namei -nom /home/webalive/myproject/myproject.sock
cd ~/myproject
gunicorn --bind 0.0.0.0:8000 myproject.wsgi
source myprojectenv/bin/activate
cd ~/myproject
gunicorn --bind 0.0.0.0:8000 myproject.wsgi
gunicorn --bind 0.0.0.0:80 myproject.wsgi
gunicorn --bind 0.0.0.0:8000 myproject.wsgi
deactivate
sudo nano /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn
sudo journalctl -u gunicorn
sudo nano /etc/nginx/sites-available/myproject
sudo rm /etc/nginx/sites-enabled/myproject
sudo rm /etc/nginx/sites-enabled/default
LS
ls
cd /etc/nginx/
ls
cd sites-enabled/
ls
cd ..
cd sites-
cd sites-available/
ls
rm default 
sudo rm default 
sudo rm myproject 
sudo rm /etc/nginx/sites-enabled/myproject
sudo nano /etc/nginx/sites-available/myproject
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'
sudo apt install certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/hsjt.com.br
sudo nginx -t
sudo systemctl reload nginx
sudo ufw status
sudo ufw allow 'Nginx Full'
sudo ufw delete allow 'Nginx HTTP'
sudo ufw status
sudo certbot --nginx -d app.hsjt.com.br
sudo systemctl status certbot.timer
sudo certbot renew --dry-run
sudo certbot --nginx -d app.hsjtmt.com.br
cd hoe
cd home
cd ~/
ls
cd myproject/
ls
cd myprojectenv/bin/
source activate
cd ..
ls
manage.py createpp auth
python manage.py createpp auth
python manage.py startpp auth
python manage.py startapp auth
ls
mkdir template
systenclt gunicorn restart
systemclt gunicorn restart
systemctl gunicorn restart
sudo systemctl restart gunicorn
ls
cd ..
ls
cd ..
çs
ls
cd webalive/
ls
cd myproject/
ls
sudo systemctl restart gunicorn
ls
cd myproject/
ls
cd myprojectenv/
cd bin
source activate
cd ..
ls
python3 manage.py startapp checkin-entrada
python3 manage.py startapp checkin
ls
git config --get-all user.name
git config --global user.name "lucasti-cba"
git config --global user.email "lucasti-cba@outlook.com"
ls
cd ..
çs
ls
git init
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/lucasti-cba/webapp-hsjt.git
git push -u origin main
