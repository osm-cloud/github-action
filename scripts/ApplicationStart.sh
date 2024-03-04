#!/bin/bash
cd /home/ec2-user
chmod 777 app.pyc

nohup python3 app.py > /dev/null 2>&1  &

