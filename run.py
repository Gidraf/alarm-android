from datetime import datetime, timedelta
import json
from nntplib import ArticleInfo
import os
from time import time
from flask import Flask, jsonify, render_template,request
import sqlite3

from service import get_article
from dateutil import parser


app = Flask(__name__,instance_relative_config=True)



@app.route("/", methods=["GET","POST"])
def home():
    # con = sqlite3.connect('articles.db')
    # cur = con.cursor()
    if request.method == "GET":
        # articles = cur.execute('''Select * from articles''').fetchall()
        # import pdb; pdb.set_trace()
        # articles  = []
        # for r in query:
        #     print(r.url)
        # import pdb; pdb.set_trace()
        return render_template("home.html",), 200
    else:
        url = request.form.get("url")
        time = request.form.get("time")
        # eta=parser.parse(time)
        # print(datetime.strptime(time))
        # get_article.apply_async(args=[url, time], eta=eta)
        eta = datetime.utcnow() + timedelta(minutes=int(time))
        get_article.apply_async(args=[url, time], eta=eta)
        # import pdb; pdb.set_trace()
        return render_template("success.html",sucess="get"), 200

if __name__ == "__main__":
    app.run(debug=True)
