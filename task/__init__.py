from task.views import app


@app.cli.command('init_db')
def init_db():
    from task import models
    models.init_db()
