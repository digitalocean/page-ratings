#!/bin/bash

set -e

virtualenv virtualenv
source virtualenv/bin/activate
pip install mysql-connector-python
deactivate
