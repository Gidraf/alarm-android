from datetime import datetime, timedelta
from flask import Flask, render_template,request
from service import get_article
import arrow

app = Flask(__name__,instance_relative_config=True)

@app.route("/", methods=["GET","POST"])
def home():

    if request.method == "GET":
        return render_template("home.html",), 200
    else:
        url = request.form.get("url")
        time = request.form.get("time")
        # import pdb; pdb.set_trace()
        eta =arrow.get(time).datetime + timedelta(seconds=10)
        
        get_article.apply_async(args=[url, time], eta=eta)
        return render_template("success.html",sucess="get"), 200

if __name__ == "__main__":
    app.run(debug=True)
