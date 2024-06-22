from flask import Flask, render_template, redirect, url_for, request
import sqlite3
from os import name
app = Flask(__name__)


conn = sqlite3.connect('use_db1')
c = conn.cursor()




conn.commit()
conn.close()



@app.route('/')
def index1():
    return render_template('index1.html',database = database)


class SQLManager:
    pass