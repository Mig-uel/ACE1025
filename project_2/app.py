from datetime import datetime, timezone
from decimal import Decimal
from math import floor

from constants import DB_URI, SECRET_KEY
from flask import Flask, abort, redirect, render_template, request, session, url_for
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import errors
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from utils.cart_utils import get_cart_items, init_cart
from utils.sanitize import check_login, check_registration

# init Flask
app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)


# ----- Models -----
# User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(8), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    isAdmin = db.Column(db.Boolean, default=False)
    orders = db.relationship("Order", backref="user", lazy=True)


# Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    category = db.relationship("Category")


# Order
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    status = db.Column(db.String(20), default="pending")
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
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


# Category
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True, nullable=False)


@app.route("/")
def home():
    year = datetime.now().year
    query = select(Product).limit(limit=4)
    products = db.session.scalars(query).all()

    query = select(Category)
    categories = db.session.scalars(query).all()

    return render_template(
        "index.html", products=products, year=year, categories=categories
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    form_errors = []

    if "user_id" in session:
        return redirect(url_for("home"))

    if request.method == "POST":
        try:
            user_data = check_registration(form=request.form)

            hashed_password = bcrypt.generate_password_hash(
                user_data["password"]
            ).decode("utf-8")

            user = User(
                username=user_data["username"],
                email=user_data["email"],
                password=hashed_password,
                first_name=user_data["first_name"],
                last_name=user_data["last_name"],
            )

            db.session.add(user)
            db.session.commit()

            session["user_id"] = user.id
            session["username"] = user.username
            session["is_admin"] = user.isAdmin
            session.setdefault(init_cart())

            return redirect(url_for("home"))
        except IntegrityError as e:
            db.session.rollback()
            orig = e.orig

            # Check if it's a UNIQUE violation
            if isinstance(orig, errors.UniqueViolation):
                msg = str(orig)
                if "user_username_key" in msg:
                    form_errors.append("That username is already taken")
                elif "user_email_key" in msg:
                    form_errors.append("That email is already registered")
            else:
                form_errors.append("Something went wrong, please try again")

        except SQLAlchemyError as e:
            db.session.rollback()
            form_errors.append(e)
        except Exception as e:
            print(type(e))
            print(e)

            for i in e.args[0]:
                form_errors.append(i)

    return render_template("register.html", errors=form_errors)


@app.route("/login", methods=["GET", "POST"])
def login():
    form_errors = []

    if "user_id" in session:
        return redirect(url_for("home"))

    if request.method == "POST":
        try:
            user_data = check_login(request.form)

            query = select(User).where(User.username == user_data["username"])
            user = db.session.scalar(query)

            if not user or (
                user
                and not bcrypt.check_password_hash(user.password, user_data["password"])
            ):
                form_errors.append("Invalid username/password")
                return render_template("login.html", errors=form_errors)

            session["user_id"] = user.id
            session["username"] = user.username
            session["is_admin"] = user.isAdmin
            session.setdefault("cart", init_cart())

            return redirect(url_for("home"))
        except Exception as e:
            for i in e.args[0]:
                form_errors.append(i)

    return render_template("login.html", errors=form_errors)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/cart")
def cart():
    if not session:
        return redirect(url_for("login"))

    return render_template(
        "cart.html",
    )


@app.patch("/cart/update")
def update_cart():
    action = request.form.get("action")
    product_id = request.form.get("product_id")

    cart = session.get("cart")
    cart_items = get_cart_items(cart)
    total_items = cart["total_items"]
    subtotal = Decimal(cart["subtotal"])

    # find item in cart_items
    item = cart_items.get(product_id)

    if action == "increase":
        total_items += 1
        item["qty"] += 1
        item["total_price"] = item["qty"] * item["price"]
        subtotal += Decimal(item["price"])
        cart_items[product_id] = item
    elif action == "decrease":
        total_items -= 1
        subtotal -= Decimal(item["price"])

        if item["qty"] == 1:
            cart_items.pop(product_id, None)
        else:
            item["qty"] -= 1
            item["total_price"] = item["qty"] * item["price"]
            cart_items[product_id] = item
    else:
        return

    cart["total_items"] = total_items
    cart["subtotal"] = subtotal
    session["cart"] = cart

    return render_template(
        "partials/cart_update_response.html",
    )


@app.post("/cart/add")
def add_to_cart():
    product_id = request.form.get("product_id")

    if not product_id:
        abort(400)

    product = db.session.get(Product, product_id)

    if not product:
        abort(400)

    cart = session.get("cart", init_cart())
    cart_items = get_cart_items(cart)
    cart_total_items = cart["total_items"]
    cart_subtotal = cart["subtotal"]

    item = cart_items.get(
        product_id,
        {
            "name": product.name,
            "qty": 0,
            "price": product.price,
            "total_price": 0,
            "image_url": product.image_url,
        },
    )

    cart_total_items += 1
    item["qty"] += 1
    item["total_price"] = item["qty"] * product.price
    cart_subtotal += item["price"]
    cart_items[product_id] = item
    cart["total_items"] = cart_total_items
    cart["subtotal"] = cart_subtotal
    session["cart"] = cart

    return render_template("partials/cart_count.html")


@app.route("/shop")
def shop():
    limit = 6
    skip = None
    query = None
    isFiltered = False
    total_count = None
    total_pages = None
    categories = Category.query

    # search params
    page = request.args.get("page", default=1, type=int)
    category = request.args.get("category", type=int)

    skip = (page - 1) * limit

    if category:
        isFiltered = True
        total_count = Product.query.filter_by(category_id=category).count()
        query = select(Product).where(Product.category_id == category).offset(skip)
    else:
        total_count = Product.query.count()
        query = select(Product).limit(limit).offset(skip)

    products = db.session.scalars(query).all()

    # calculate pages
    total_pages = floor(total_count / limit) or 1

    return render_template(
        "shop.html",
        products=products,
        isFiltered=isFiltered,
        total_count=total_count,
        total_pages=total_pages,
        page=page,
        categories=categories,
    )


@app.route("/shop/<int:id>")
def single_product(id):
    try:
        query = select(Product).where(Product.id == id)
        product = db.session.scalar(query)

        if not (product):
            raise Exception("Product not found")

        return render_template("single_product.html", product=product)
    except Exception as e:
        print(e)
        return abort(404)


@app.route("/orders")
def orders():
    if not session:
        return redirect(url_for("login"))

    return "orders page"


@app.route("/checkout")
def checkout():
    return render_template("checkout.html")


@app.route("/admin")
def admin():
    print(session)
    if not session or not session["is_admin"]:
        return redirect(url_for("home"))

    return "admin page"


@app.errorhandler(404)
def not_found(e):
    return render_template("not_found.html")


if __name__ == "__main__":
    app.run(debug=True)
