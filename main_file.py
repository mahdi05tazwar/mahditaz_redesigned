from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/Index")
def indexredirect():
    return redirect(url_for("index"))

@app.route("/")
def noname():
    return redirect(url_for("index"))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/About")
def aboutredirect():
    redirect(url_for("about"))

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/Contact")
def contactredirect():
    redirect(url_for("contact"))

@app.route("/<name>")
def incorrectloc(name):
    if name != "" or name != "home" or name != "about" or name != "contact":
        return render_template("incorrectloc.html")

@app.route("/flappybirdhd_ss")
def flappybirdhd_ss():
    return render_template("fb_ss.html")

@app.route("/gmailauto_ss")
def gmailauto_ss():
    return render_template("gmau_ss.html")

@app.route("/pongpong_ss")
def pongpong_ss():
    return render_template("p_ss.html")

@app.route("/htmlassistant_ss")
def htmlassistant_ss():
    return render_template("ha_ss.html")


if __name__ == "__main__":
    app.run(debug = True)