from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)


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
    app.run(debug=True)
