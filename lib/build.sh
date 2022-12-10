#!/bin/sh
# Install dependencies
cd mysql-connector-python
apt-get install software-properties-common
add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.8
python setup.py install