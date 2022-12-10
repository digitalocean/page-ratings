#!/bin/sh
# Install dependencies

set -e

virtualenv --without-pip virtualenv
pip install mysql-connector-python --target virtualenv/lib/python3.9/site-packages
