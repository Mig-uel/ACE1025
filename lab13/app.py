import os

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

load_dotenv()  # read .env file
DB_URI = os.getenv("DB_URI")

app = Flask(__name__)

# connect to Postgres
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TACK_MODIFICATIONS"] = False

# create a db object
db = SQLAlchemy(app)


# define a model (create table in the demoDB db)
class UserLogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)


@app.route("/")
def index():
    fruits = [
        "apple",
        "orange",
        "grapes",
    ]
    return render_template("index.html", fruits_list=fruits)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/users")
def users():
    return render_template("users.html")


@app.route("/quotes")
def quotes():
    return redirect(url_for("index"))


@app.route("/user/<name>")
def user(name):
    return render_template("index.html", username=name)


# set the 'app' to run if you execute the file directly(not when it is imported)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
