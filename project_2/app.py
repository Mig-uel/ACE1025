from datetime import datetime

from constants import DB_URI
from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from utils.sanitize import check_registration

# init Flask
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)


# ----- Models -----
# User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(8), nullable=False, unique=True)
    email = db.Column(db.String(25), nullable=False, unique=True)
    isAdmin = db.Column(db.Boolean, default=False)


# Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    qty = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String(255))


# Order
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.String(20), default="pending")
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
    user = db.relationship("User", backref=db.backref("orders", lazy=True))
    items = db.relationship(
        "OrderItem", backref="order", lazy=True, cascade="all, delete-orphan"
    )


# OrderItem
class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    qty = db.Column(db.Integer, nullable=False, default=1)
    price = db.Column(db.Numeric(10, 2), nullable=False)


@app.route("/")
def home():
    query = select(Product).where()
    boxes = db.session.scalars(query)

    return render_template("index.html", products=boxes.all())


@app.route("/register", methods=["GET", "POST"])
def register():
    errors = None
    if request.method == "POST":
        try:
            check_registration(form=request.form)
        except Exception as e:
            errors = e.args[0]

    return render_template("register.html", errors=errors)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/cart")
def cart():
    return "cart route"


@app.route("/shop")
def shop():
    return "shop route"


@app.route("/shop/<id>")
def single_product(id):
    return f"single product route {id}"


@app.errorhandler(404)
def not_found(e):
    return "not found"


if __name__ == "__main__":
    app.run(debug=True)
