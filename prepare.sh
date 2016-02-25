#!/bin/sh

sudo apt-get install build-essential python-dev python-pip libffi-dev -y
pip install -r requirements.txt
pip install --upgrade cffi #fix bug 'No module named setuptools_ext'
