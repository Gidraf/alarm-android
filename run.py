import os
from flask import Flask, render_template

app = Flask(__name__,instance_relative_config=True)

app.route("/")
def home():
    return render_template("home.html"), 200

if __name__ == "__main__":
    app.run(debug=True)
