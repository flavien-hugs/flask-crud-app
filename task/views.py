from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def index():
    return render_template("pages/index.html")


@app.route("/about/")
def about():
    return render_template("pages/about.html")
