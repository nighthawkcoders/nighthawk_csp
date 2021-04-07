# Deployment Guide

## Setup Virtual environment and clone code from GitHub
#### In console/terminal (first time only: setup environment)...

pi@raspberrypi:~ $  ``` sudo apt update; sudo apt upgrade```

pi@raspberrypi:~ $  ``` sudo apt install python3-pip nginx```

pi@raspberrypi:~ $  ``` sudo pip3 install virtualenv```

pi@raspberrypi:~ $  ``` cd ~```

```diff
- This clone and cd name MUST change to matcch your repository
+ REPLACE with flask-idea-homesite with your repo name
```

pi@raspberrypi:~ $  ```git clone https://github.com/nighthawkcoders/flask-idea-homesite```

pi@raspberrypi:~ $  ```cd ~/flask-idea-homesite```

#### Activate virual environment prior to updating packages...

pi@raspberrypi:~/flask-idea-homesite $  ```virtualenv -p /usr/bin/python3 homesite```

#### pip install and/or requirements.txt (if you have one) to satisfy dependencies...

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ```  pip install gunicorn```

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ```  pip install -r requirements.txt```

#### Start an application test server, if it fails pip install dependency

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ``` python main.py ``` 

#### Test in browser ...

http://localhost:8080/ 

stop test server by typing control-c in terminal

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ``` ^c ``` 

#### Virual environment is ready, this is how you get out of virualenv and return to home directory...

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ``` deactivate```

pi@raspberrypi:~/flask-idea-homesite $  ``` cd```


### Build Gunicorn configuration file.  Interesting bits...
<ol>
<li> 'ExecStart' start statement looks into wsgi:app (wsgi.py) and starts localhost:8080 as defined in file. </li>
<li> 'ExecStart' -workers 3 starts thread processes that are listening for connections, this ties into load balancing. </li>
</ol>
#### In console/terminal with nano, vi, or other text editor (first time only: setup Gunicorn configuration file)...

pi@raspberrypi:~ $  ``` sudo nano /etc/systemd/system/homesite.service```

    [Unit]
    Description=Gunicorn instance to serve homesite web project
    After=network.target

    [Service]
    User=pi
    Group=www-data
    WorkingDirectory=/home/pi/flask-idea-homesite
    Environment="PATH=/home/pi/flask-idea-homesite/homesite/bin"
    ExecStart=/home/pi/flask-idea-homesite/homesite/bin/gunicorn --workers 3 --bind unix:homesite.sock -m 007 wsgi:app

    [Install]
    WantedBy=multi-user.target

### Build Nginx configuration file.  Requirements [Internet Domain](https://docs.google.com/document/d/1nODveWp0jBzj4ZpFLgWCWTOXzLAHAPUhAQYmZJ4LhyU/edit), Host IP address, [Internet IP address](http://127.0.0.1:8080/pi/portforward).
<ol>
  <li> Obtain your own 'server_name' values; these VALUES WILL NOT WORK for your environment</li>
  <li> 'listen' is the port for nginx, this port will be used when you port forward </li>
  <li> 'proxy_pass' is passing connect along to gunicorn server </li>
</ol>

```diff
- THESE server_name values MUST CHANGE to match your solution:  
- nighthawkcoders.cf 192.168.1.245 70.95.179.231
+ REPLACE with yourdomain.com yourpublic-ip
```
#### In console/terminal with nano, vi, or other text editor (first time only: setup Nginx configuration file)...

pi@raspberrypi:~ $  ``` sudo nano /etc/nginx/sites-available/homesite```

    server {
        listen 80;
        server_name nighthawkcoders.cf 70.95.179.231;

        location / {
            include proxy_params;
            proxy_pass http://unix:/home/pi/flask-idea-homesite/homesite.sock;
        }
    }


## Prepare for Gunicorn usage and verify
#### In console/terminal test Gunicorn test Server and virify (first time only: gunicor exectuion)...

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ```homesite/bin/gunicorn --bind 0.0.0.0:8080 wsgi:app```

in your browser ...

http://localhost:8080/ 

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ``` ^c ``` 


## Validate Gunicorn configuration file and enable service permanently
#### In console/terminal start Gunicorn

```diff
- This service file name MUST CHANGE to match your name of your gunicorn service 
+ REPLACE with <filename>.service
```

pi@raspberrypi:~ $ ```sudo systemctl start homesite.service```

pi@raspberrypi:~ $ ```sudo systemctl enable homesite.service```
 
check the status...

pi@raspberrypi:~ $ ```sudo systemctl status homesite.service```

stop status by typing q in terminal


## Validate Nginx configuration file and enable service permanently
#### In console/terminal start Nginx

link file...

pi@raspberrypi:~ $ ```sudo ln -s /etc/nginx/sites-available/homesite /etc/nginx/sites-enabled```

test for errors...

pi@raspberrypi:~ $ ```sudo nginx -t```

start the web server...

pi@raspberrypi:~ $ ```sudo systemctl restart nginx```

check nginx status...

pi@raspberrypi:~ $ ```sudo systemctl status nginx```

stop status by typing q in terminal

in address bar of browser on another device in LAN type IP address of this Nginx server ...

```diff
- This IP address MUST CHANGE to match your Raspberry Pi 
+ REPLACE with yourpi-ip
```
http://192.168.1.245/
