#!/bin/bash

/usr/bin/apt update -y
/usr/bin/apt upgrade -y

#Install Python3
/usr/bin/apt install -y python3

#Install git
/usr/bin/apt install -y git

#Install nginx
/usr/bin/apt install -y nginx
/usr/bin/apt start nginx


