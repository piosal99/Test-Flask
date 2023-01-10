import requests
import configparser
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/todo-list')
def home():
    return render_template("index.html")
"""""
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))
"""""





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
