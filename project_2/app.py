from constants import DB_URI
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# init Flask
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(8), nullable=False, unique=True)
    email = db.Column(db.String(25), nullable=False, unique=True)


@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
