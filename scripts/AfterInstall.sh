#!/bin/bash
yum install -y python3-pip
pip3 install flask
mkdir -p /var/log/app/
chmod 777 app.pyc