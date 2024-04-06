import os
import sys


# Global settings

DEBUG = True
MAIN_DIR = os.path.abspath(os.path.join(os.path.dirname(sys.executable), os.pardir)) if not DEBUG \
            else os.path.abspath(os.path.join(os.path.dirname(sys.executable), os.pardir, os.pardir))

# DB settings

DB_DIR = f'{MAIN_DIR}/src/server/database'
DB_NAME = f'Bolnica.db'

# Server settings 

HOST = '127.0.0.1'
PORT = 8000
URL = f'http://{HOST}:{PORT}'

# Client settings

IMG_PATH = f'{MAIN_DIR}/src/client/img'
