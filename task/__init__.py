from task.views import app
from task import models


models.db.init_app(app)

@app.cli.command('init_db')
def created_db():
    models.init_db()
