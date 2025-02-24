from flask import Flask, render_template, Response, request
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("cal.html")

if __name__ == "__main__":
    app.run(host="localhost")