from flask import Flask, redirect, url_for, render_template, request, json
import pandas as pd
import numpy as np

app=Flask(__name__)

### Web Pages ###
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)