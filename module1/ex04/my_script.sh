#! /bin/sh

virtualenv -p $(which python3) django_venv
source $(PWD)/django_venv/bin/activate
pip3 install -r requirements.txt

# Launch with source