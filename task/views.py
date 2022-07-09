# task.views.py

from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)
app.config.from_object('config')


@app.route("/")
def index():
    return render_template("pages/index.html")


@app.route("/about/")
def about():
    return render_template("pages/about.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('pages/page_not_found.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('pages/page_not_found.html'), 500
