#python manage.py runserver
#python manage.py startapp roster_1
#cd C:\Python\pythonProject\django_ROSTER\roster
#python manage.py makemigrations   python manage.py migrate
#python manage.py createsuperuser

# Kroy    GK
# guest   Grey Knights
#ghEregerErger342

#mkdir Desktop

#command = '/home/denis/gk/sait_pro_Warhammer/env/bin/gunicorn'
#pythonpath = '/home/denis/gk/sait_pro_Warhammer/roster'
#bind = 'u.lv426.tech:31080'
#workers = 15
#user = 'denis'
#limit_request_fields = 32000
#limit_request_field_size = 0
#raw_env = 'DJANGO_SETTINGS_MODULE=roster.settings'


#nano /home/denis/gk/sait_pro_Warhammer/roster/gunicorn_config.py


#mkdir /home/denis/gk/sait_pro_Warhammer/bin


# #!/bin/bash
#source /home/denis/gk/sait_pro_Warhammer/env/bin/activate
#exec gunicorn -c /home/denis/gk/sait_pro_Warhammer/roster/gunicorn_config.py siteparser.wsgi

#location / {
#    proxy_pass http://127.0.0.1:31080;
#    proxy_set_header X-Forwarded-Host $server_name;
#    proxy_set_header X-Real-IP $remote_addr;
#    add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
#    add_header Access-Control-Allow-Origin *;
#}

#. env/bin/activate

#sudo nano /etc/supervisor/conf.d/roster.conf

#[program:gunicorn]
#command=/home/denis/gk/sait_pro_Warhammer/bin/start_gunicorn.sh
#user=denis
#process_name=%(program_name)s
#numproc=1
#autostart=1
#autorestart=1
#redirect_stderr=true


#location /static/ {
#    alias /home/denis/gk/sait_pro_Warhammer/env/lib/python3.10/site-packages/django/contrib/admin/static/;
#    expires modified +1w;
#}

# sudo mkdir gk/sait_pro_Warhammer/roster

# cd gk/sait_pro_Warhammer
# nano bammer/

#

#. env/bin/activate               . env/bin/deactivate
#nohup ./manage.py runserver 0.0.0.0:31080    nohup ./manage.py runserver 0.0.0.0:31080 </dev/null &>/dev/null &


#z_inf.html

#nano server.py

#gunicorn -b 0.0.0.0:31080 server:process_http_request


#def process_http_request(environ, start_response):
#    status = '200 OK'
#    response_headers = [
#        ('Content-type', 'text/plain; charset=utf-8'),
#    ]
#    start_response(status, response_headers)
#    text = 'Here be dragons'.encode('utf-8')
#    return [text]

#gunicorn --bind u.lv426.tech:31080 roster.wsgi
#gunicorn --bind 0.0.0.0:31080 roster.wsgi

#gunicorn testproj.wsgi:application --bind 0.0.0.0:31080
#gunicorn roster.wsgi:application --bind 0.0.0.0:31080

#if settings.DEBUG:
#    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


############################

#git clone https://github.com/LaienSicet/sait_pro_Warhammer.git

#sudo apt update
#sudo apt upgrade
#sudo apt install -y vim mosh tmux htop git curl wget unzip zip gcc build-essential make

#sudo localedef ru_RU.UTF-8 -i ru_RU -fUTF-8 ; \
#export LANGUAGE=ru_RU.UTF-8 ; \
#export LANG=ru_RU.UTF-8 ; \
#export LC_ALL=ru_RU.UTF-8 ; \
#sudo locale-gen ru_RU.UTF-8 ; \
#sudo dpkg-reconfigure locales

#sudo apt install -y zsh tree redis-server nginx libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-dev python3-pil python3-lxml libxslt-dev python3-libxml2 libffi-dev libssl-dev python-dev gnumeric libsqlite3-dev libpq-dev libxml2-dev libxslt1-dev libjpeg-dev libfreetype6-dev libcurl4-openssl-dev supervisor

#chsh -s $(which zsh)

#apt install python3

#/usr/bin/python3.10 -m venv env

#. env/bin/activate
#pip install -U pip
#pip install django
#pip freeze > requirements.txt   а надоли?

#nano settings.py
        #ALLOWED_HOSTS = ['u.lv426.tech', '127.0.0.1']

#./manage.py runserver 0.0.0.0:31080

pip install gunicorn
pip freeze > ../requirements.txt
nano gunicorn_config.py

/home/denis/gk/sait_w/env/bin/
/home/denis/gk/sait_w/roster/
/home/denis/gk/sait_w/
chmod +x start_gunicorn.sh

command = '/home/denis/gk/sait_w/env/bin/gunicorn'
pythonpath = '/home/denis/gk/sait_w/roster'
bind = 'u.lv426.tech:31080'
workers = 15
user = 'denis'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=roster.settings'

mkdir bin
nano start_gunicorn.sh

#!/bin/bash
source /home/denis/gk/sait_w/env/bin/activate
exec gunicorn -c /home/denis/gk/sait_w/gunicorn_config.py roster.wsgi


location / {
    proxy_pass http://u.lv426.tech:31080;
    proxy_set_header X-Forwarded-Host $server_name;
    proxy_set_header X-Real-IP $remote_addr;
    add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
    add_header Access-Control-Allow-Origin *;
}


. start_gunicorn.sh



command = '/home/denis/gk/sait_w/env/bin/gunicorn'
pythonpath = '/home/denis/gk/sait_w/roster'
bind = '0.0.0.0:31080'
workers = 15
user = 'denis'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=roster.settings'



location /static/ {
    alias /home/denis/gk/sait_w/roster/roster_1/;
    expires modified +1w;
}


chmod 755 /home/denis


sudo nano /etc/supervisor/conf.d/roster.conf

[program:gunicorn]
command=/home/denis/gk/sait_w/bin/start_gunicorn.sh
user=denis
process_name=%(program_name)s
numproc=1
autostart=1
autorestart=1
redirect_stderr=true


sudo service supervisor stop

sudo service supervisor start

CSRF_TRUSTED_ORIGINS = ['http://u.lv426.tech']