import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SECRET_KEY = os.environ.get('secret') or 'you-will-never-guess'
    DB_USER = os.environ.get('db_user')
    DB_PASS = os.environ.get('db_pass')
    DB_DB = os.environ.get('db_db')
    DB_PATH = os.environ.get('db_path')
    WEB_PATH = '3.65.38.102:5000'
