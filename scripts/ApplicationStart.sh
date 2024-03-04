#!/bin/bash
cd /home/ec2-user
python3 -m compileall ./app.py
mv ./__pycache__/*.pyc ./app.pyc