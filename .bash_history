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
