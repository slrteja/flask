from functools import wraps
from flask import Flask, redirect,render_template,redirect,session
import pymongo

app=Flask(__name__)
app.secret_key="abcdefghijklmnopqrstuvwxy"

client=pymongo.MongoClient('127.0.0.1',27017)
db=client.sankar

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
        
    return wrap

from user import routes

@app.route('/') 
def home():
    return render_template('home.html')

@app.route('/dashboard/' , methods=['GET', 'POST']) 
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/edit/')
@login_required
def table():
    return render_template('table.html')

@app.route('/marks/',methods=['GET', 'POST'])
@login_required
def marks():
    return render_template('marks.html')

