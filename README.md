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



