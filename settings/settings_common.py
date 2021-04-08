#!/usr/bin/env/python
# Common settings are definde here. only upper case allowed

#imports
import os

APP_ROOT = os.path.dirname(os.path.dirname(__file__))
DB_NAME = 'main.db'
DATABASE = os.path.join(APP_ROOT, DB_NAME)