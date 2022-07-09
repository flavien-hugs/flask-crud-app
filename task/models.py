# task.models.py

import logging as lg
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=True,
        default=datetime.utcnow()
    )

    def __repr__(self):
        return f"Tâche: {self.name}"


def init_db():
    db.create_all()
    lg.warning('Database initialized !')
