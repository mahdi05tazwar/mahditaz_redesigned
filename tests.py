from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "<H1 style = \"font-family: Helvetica;\">HEY</H1>"

@app.route("/about")
def about():
    return "<H1 style = \"font-family: Helvetica;\">HEY</H1>"

@app.route("/contact")
def contact():
    return "<H1 style = \"font-family: Helvetica;\">HEY</H1>"

@app.route("/<name>")
def namer(name):
    return f"{name}"

@app.route("/admin")
def admin():
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()