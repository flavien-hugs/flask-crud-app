# task.config.py

import os

SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False

if os.getenv('DATABASE_URL'):
   SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
else:
   BASE_DIR = os.path.abspath(os.path.dirname(__file__))
   SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, 'tasks.db')
