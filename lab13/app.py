import os

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for
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


# define an employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(6), unique=True, nullable=False)
    employee_name = db.Column(db.String(50), nullable=False)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return f"<div><h1>Successfully Submitted</h1><p>Username: {request.form['username']}</p><p>Password: {request.form['password']}</p><a href='{request.base_url}'>Go Home</a><div>"

    fruits = [
        "apple",
        "orange",
        "grapes",
    ]
    return render_template("index.html", fruits_list=fruits)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "POST":
        form = request.form
        id = form["employee_id"]
        name = form["employee_name"]

        # create a new employee object
        employee = Employee(employee_id=id, employee_name=name)

        db.session.add(employee)
        db.session.commit()

        return render_template("submitted.html", name=name)

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
