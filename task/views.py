# task.views.py

from datetime import datetime
from flask import(
    Flask, request, redirect, flash,
    render_template
)
from task.models import db, Task


app = Flask(__name__)
app.config.from_object('config')


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form['name']
        if not name:
            flash('Définir la tâche a ajoutée !')
        try:
            new_task = Task(name=name)
            db.session.add(new_task)
            db.session.commit()
            flash(f"Nouvelle tâche <b>'{name}'</b> ajoutée !")
            return redirect("/")
        except Exception as e:
            return f"Une erreur s'est produite: {e}"

    tasks = Task.query.order_by(Task.created_at)
    return render_template("pages/create.html", tasks=tasks)


@app.route("/delete/<int:id>/")
def deleteTask(id):
    task = Task.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        flash(f"La tâche <b>'{task.name}'</b> a été supprimé !")
        return redirect("/")
    except Exception as e:
        return f"Une erreur s'est produite: {e}"


@app.route("/update/<int:id>/", methods=["GET", "POST"])
def updateTask(id):
    task = Task.query.get_or_404(id)
    if request.method == "POST":
        task.name = request.form['name']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return "Cette tâche ne peut-être modifier !"
    else:
        page_tile = "Mettre à jour de la tâche"
        return render_template('pages/update.html', page_tile=page_tile, task=task)


@app.route("/about/")
def about():
    return render_template("pages/about.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('pages/page_not_found.html', error=error), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('pages/page_not_found.html', error=error), 500
