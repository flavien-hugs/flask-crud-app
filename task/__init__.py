from task.views import app
from task.models import db, init_db


db.init_app(app)

@app.cli.command('init_db')
def created_db():
    init_db()
