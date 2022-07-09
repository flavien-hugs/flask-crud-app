# task.config.py

import os
import re

SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False

if os.environ.get('DATABASE_URL') is None:
   BASE_DIR = os.path.abspath(os.path.dirname(__file__))
   SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, 'tasks.db')
else:
   uri = os.getenv("DATABASE_URL")
   if uri.startswith("postgres://"):
      uri = uri.replace("postgres://", "postgresql://", 1)
      # SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
