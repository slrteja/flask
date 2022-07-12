from flask import Flask,render_template
from app import app,login_required
from user.models import User

@app.route('/user/signup/', methods=['POST'])
def signup():
    return User().signup()

@app.route('/user/signout/')
def signout():
    return User().signout()

@app.route('/user/signin/' ,methods = ['POST'])
def signin(): return User().signin()

@app.route('/user/marks/',methods = ['GET','POST'])
def mark(): return User().emp()