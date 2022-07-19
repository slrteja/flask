from flask import Flask, flash, jsonify,render_template,request,url_for,redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
from sqlalchemy import true

app = Flask(__name__)
app.secret_key = "8756aefasaf1e567huhgybhjbuy8945"

client = MongoClient('localhost', 27017)

db = client.company
teja = db.teja

# ...

@app.route('/', methods=('GET','POST','PUT'))
def index():
    print(request.form)
    if request.method=='POST':
            user={
            "name" : request.form.get('name'),
            "gender" : request.form.get('gender'),
            "email": request.form.get('email'),
        }
            if db.teja.find_one({"email": user["email"]}):
                db.teja.update_one({"email": "email"},{"$set": {"name": "name", "email": "email","gender": "gender"}},upsert=True)
                return jsonify("error data already exists")
            elif db.teja.insert_one(user):
                flash('Thanks for adding this information')
            return redirect(url_for('index'))
    all_teja = teja.find()
    return render_template('index.html', teja=all_teja)
    
        
# ...

@app.post('/<id>/delete/')
def delete(id):
    teja.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

# ...
@app.post('/update/')
def put(id,name, email, gender):
    
        
    teja.find_one_and_update({"email": email},{"$set": {"name": name, "email": email,"gender": gender}},upsert=True)
    return redirect(url_for('index'))

#...

@app.route('/edit/')
def edit():
    if request.method=='POST':
        id= request.form['_id']
        uname = request.form['name']
        uemail=request.form['email']
        ugender = request.form['gender']
    return  render_template('/edit.html')

if __name__ == "__main__":
    app.run(debug=true)