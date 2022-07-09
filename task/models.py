# task.models.py

import logging as lg
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from task.views import app

db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=True,
        default=datetime.utcnow()
    )

    def __init__(self, name, created_at):
        self.name = name
        self.created_at = created_at

    def __repr__(self):
        return f"Tâche: {self.name}"


def init_db():
    db.drop_all()
    db.create_all()
    task = Task(name="Apprendre le micro-framework Flask", created_at=datetime.utcnow())
    task_one = Task(name="Apprendre le framework Django", created_at=datetime.utcnow())
    db.session.add(task)
    db.session.add(task_one)
    db.session.commit()
    lg.warning('Database initialized !')
