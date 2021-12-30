{% include navigation.html %}

# <img src="static/assets/ncs_logo.png" height="60" alt=""> GitHub Activity
### <a href="https://github.com/nighthawkcoders/nighthawk_csp/graphs/contributors" target="_blank">CSP Repo Insights</a>

<table>
  <tr>
    <th>Name</th>
    <th>Profile</th>
    <th>Issues</th>
    <th>Commits</th>
  </tr>
  <tr>
    <td>John Mortensen</td>
    <td><a href="https://github.com/jm1021" target="_blank">Profile</a></td>
    <td><a href="https://github.com/nighthawkcoders/nighthawk_csp/issues?q=assignee%3Ajm1021" target="_blank">Issues</a></td>
    <td><a href="https://github.com/nighthawkcoders/nighthawk_csp/commits?author=jm1021" target="_blank">Commits</a></td>
  </tr>
</table>


# Deployment Guide

## Raspberry Pi (RPi) Purchase and Setup
<details>
  <summary>Click for Raspberry Pi 4 purchase!</summary>

### RPi recommended specs
<OL> 
<li> Raspberry Pi 4 4GB Model B with 1.5GHz 64-bit quad-core CPU (4GB RAM) </li>
<li> 32GB Samsung EVO+ Micro SD Card (Class 10) Pre-loaded with NOOBS, USB MicroSD Card Reader </li>
<li> Raspberry Pi 4 Case </li>
<li> 3.5A USB-C Raspberry Pi 4 Power Supply (US Plug) with Noise Filter</li>
<li> Set of Heat Sinks </li>
<li> Micro HDMI to Full HDMI Cable - 6 foot (Supports up to 4K 60p) </li>
<li> USB-C PiSwitch (On/Off Power Switch for Raspberry Pi 4) </li>
</OL> 
Purchase Notes:  Keyboard, Mouse, Monitor are optional.  RPi advantages over AWS: 1. One time cost  2. All kinds of tinker projects in IOT realm can be performed using GPIO pins.  As for purchase options, CanaKit (my prefered) has options on Amazon that meet the bulleted list of requirements. There is a new option on raspberrypi.org that describes RPi as built into a keybaord (could be bulky in my use cases). 
</details>

<details>
  <summary>Click for Raspberry Pi 4 OS and Software!</summary>

RPi OS deployment preparation: RPi with NOOBS installed on SSD is very simple.  At boot select Raspberry Pi OS and you are on your way.  Since this will be private IP host on your home network, ultimately Port Forwarding is required to make your machine visible to the Internet. 

VNC Viewer can connect to the RPi for desktop display.  This is a full desktop remote display tool, SSH is a terminal only option.  RealVNC lets you share full desktop with cohorts.  If you reboot RPi, you need a monitor connected at reboot to maintain VNC screen share functionality.  Reboot will cause screen buffer not to be recognized unless HDMI is present.  There may be a dummy (mini) HDMI plug that could overcomee this issue.  Otherwise, after setup your RPi could be headless.
</details>

## AWS EC2 Setup (an alternative to RPi)
<details>
  <summary>Instruction on preparing AWS EC2 instance for Webserver deployment!</summary>
  
Login into your AWS IAM user, search for EC2.

#### To get started, launch an Amazon EC2 instance, which is a a computer server in the cloud.
<img src="https://github.com/nighthawkcoders/flask-idea-homesite/blob/master/assets/ec2launch.png">

## Step 1: Choose an Amazon Machine Image (AMI)Cancel and Exit
#### An AMI is a template that contains the software configuration (operating system, application server, and applications) required to launch your instance. Pick Ubuntu free tier operating system that uses the Linux kernel.  Note, this is very compatible Raspberry Pi's OS.
<img src="https://github.com/nighthawkcoders/flask-idea-homesite/blob/master/assets/ec2os.png">

## Step 2: Choose an Instance Type
Amazon EC2 provides a wide selection of instance types optimized to fit different use cases. Instances have varying combinations of CPU, memory, storage, and networking capacity.   Stick with Free Tier options, as of this writing t2.mico with free tier designation is suggested.

## No action on Steps #3 through #4
Step 3: Configure Instance Details
Stick with default.  Your will launch a single instance of the AMI by using defaults

Step 4: Add Storage
Stick with default.  Your instance will be launched with 8gb of storage.

## Step 5: Add Tags
#### Tag your Amazon EC2 resources.  This is not required but you could name your volume for future identification.
<img src="https://github.com/nighthawkcoders/flask-idea-homesite/blob/master/assets/ec2tags.png">

## Step 6: Configure Security Group
#### A security group is a set of firewall rules that control the traffic for your instance. On this page, you can add rules to allow specific traffic to reach your instance. In this example, a web server is setup to allow Internet traffic to reach EC2 instance, this allows unrestricted access to the HTTP and HTTPS ports.  Also, this example restricts SSH from my IP.
<img src="https://github.com/nighthawkcoders/flask-idea-homesite/blob/master/assets/ec2security.png">

## Step 7: Review Instance Launch
#### Review your instance launch details. Click Launch to assign a key pair to your instance and complete the launch process.
<img src="https://github.com/nighthawkcoders/flask-idea-homesite/blob/master/assets/ec2keypair.png">

## Before you leave your ADMIN session on AWS go to EC2 running instances and find your IPV4 address.
#### Find IPv4 address and IPv4 DNS
<img src="https://github.com/nighthawkcoders/flask-idea-homesite/blob/master/assets/ec2ipv4.png">

# Start a terminal session on you localhost.
</details
  
<details>
  <summary>Click for Flask Web server setup!</summary>
  
## Setup Virtual environment and clone code from GitHub
#### In console/terminal (first time only: setup environment)...

pi@raspberrypi:~ $  ``` sudo apt update; sudo apt upgrade```

pi@raspberrypi:~ $  ``` sudo apt install python3-pip nginx```

pi@raspberrypi:~ $  ``` sudo pip3 install virtualenv```

pi@raspberrypi:~ $  ``` cd ~```

```diff
- This clone and cd name MUST change to matcch your repository
+ REPLACE flask-idea-homesite with your repo name
```

pi@raspberrypi:~ $  ```git clone https://github.com/nighthawkcoders/flask-idea-homesite```

pi@raspberrypi:~ $  ```cd ~/flask-idea-homesite```

#### Activate virtual environment prior to updating packages...

```diff
- The homesite name should be a name that corresponds with project for easy recall 
+ REPLACE homesite with your virtualenv preferred name
```

pi@raspberrypi:~/flask-idea-homesite $  ```virtualenv -p /usr/bin/python3 homesite```

pi@raspberrypi:~/flask-idea-homesite $  ```source homesite/bin/activate```


#### pip install and/or requirements.txt (if you have one) to satisfy dependencies...

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ```  pip install gunicorn```

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ```  pip install -r requirements.txt```

#### Verify Python virual environment and package dependencies, if it fails pip install dependency
```diff
- The main.py name should be a name that corresponds with the file you typically run in development environment, it should contain app 
+ REPLACE main.py with your <my-python-file>.py
```

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ``` python main.py ``` 

#### Test Python run in browser ...

http://localhost:8080/ 

stop test server by typing control-c in terminal

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ``` ^c ``` 

#### Verify Gunicorn instalation, In console/terminal test Gunicorn test Server...
#### Verify Python virual environment and package dependencies. If it fails pip install each missing dependency, best to get these into requirements.txt
```diff
- The main:app with file that contain Flask app 
+ REPLACE main:app with your <my-python-file>:app
```

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ```homesite/bin/gunicorn --bind 0.0.0.0:5000 main:app```

in your browser ...

#### Test Gunicorn run in browser ...

http://localhost:5000/ 

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ``` ^c ``` 


#### Virual environment is ready, this is how you get out of virualenv and return to home directory...

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ``` deactivate```

pi@raspberrypi:~/flask-idea-homesite $  ``` cd```

## Creating System Files to run your Web Application as a Service

### Build Gunicorn configuration file.

#### In console/terminal with nano, vi, or other text editor (first time only: setup Gunicorn configuration file)...
```diff
- The homesite filename and name reference, the main:app should change as discussed previously
+ REPLACE according to your project requirements
```

pi@raspberrypi:~ $  ``` sudo nano /etc/systemd/system/homesite.service```

    [Unit]
    Description=Gunicorn instance to serve homesite web project
    After=network.target

    [Service]
    User=pi
    Group=www-data
    WorkingDirectory=/home/pi/flask-idea-homesite
    Environment="PATH=/home/pi/flask-idea-homesite/homesite/bin"
    ExecStart=/home/pi/flask-idea-homesite/homesite/bin/gunicorn --workers 3 --bind unix:homesite.sock -m 007 main:app

    [Install]
    WantedBy=multi-user.target

### Build Nginx configuration file.

```diff
- THESE server_name values MUST CHANGE to match your solution:  
- nighthawkcoders.cf 70.95.179.231
+ REPLACE with yourdomain.com yourpublic-ip
```
#### In console/terminal with nano, vi, or other text editor (first time only: setup Nginx configuration file)...

pi@raspberrypi:~ $  ``` sudo nano /etc/nginx/sites-available/homesite```

    server {
        listen 80;
        listen [::]:80;
        server_name idea.nighthawkcodingsociety.com;
    
        location / {
            include proxy_params;
            proxy_pass http://unix:/home/pi/flask-idea-homesite/homesite.sock;
        }
    }

## Validate Gunicorn configuration file and enable service permanently
#### In console/terminal start Gunicorn

```diff
- This service file name MUST CHANGE to match your name of your gunicorn service 
+ REPLACE with <filename>.service
```

pi@raspberrypi:~ $ ```sudo systemctl start homesite.service```

pi@raspberrypi:~ $ ```sudo systemctl enable homesite.service```
 
check the status, if all OK enable service permanentley...

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
  
</details>




