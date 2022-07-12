
from flask import Flask,jsonify, redirect,request,session,redirect
import uuid
from passlib.hash import pbkdf2_sha256
from sqlalchemy import true
from app import db

class User:
    
    def start_session(self,user):
        session['logged_in']=True
        del user['password']
        session['user']=user
        return jsonify(user),200
    
    def signup(self):
        print(request.form)
        
        user={
            "_id": uuid.uuid4().hex,
            "id": request.form.get('id'),
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password'),
        }
        
        user["password"]=pbkdf2_sha256.encrypt(user['password'])
        
        if db.teja.find_one({"email": user["email"]}):
            return jsonify({"error": "Email already exists"}),400
        
        if db.teja.insert_one(user):
            return self.start_session(user)
        return jsonify({"error": "Signup Failed"}),400
    def signout(self):
        session.clear()
        return redirect('/')
    
    def signin(self):
        
        user=db.teja.find_one({"email": request.form.get('email')})
        if user and pbkdf2_sha256.verify(request.form.get('password'),user['password']):
            return self.start_session(user)
        return jsonify({"error": "Login Failed"}),401
    def marks(self):
        print(request.form)
        
        usermark={
            "_id": request.form.get('_id'),
            "Maths": request.form.get('Maths'),
            "Science": request.form.get('Science'),
            "Social": request.form.get('Social'),
        }
        db.teja.insert_one(usermark)
        # update usermark with   new values from db.teja table
        emp=db.teja.find({}, {"Maths": request.form.get('Maths'), "Science": request.form.get('Science')})
        return jsonify(emp=emp),200
    