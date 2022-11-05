import pymongo
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')

client = pymongo.MongoClient(
    "mongodb+srv://19bcs003:<password>@cluster0.yl324ol.mongodb.net/?retryWrites=true&w=majority")
db = client.test.users

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def login():
    return render_template('about.html')

@app.route("/signup")
def signup():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form["password"]

        if (db.find_one({"email": email})):
            return "Users already exits"
        else:
            post = db.insert_one({"email": email, "password": password})
            return render_template('signin.html')
    return render_template('signup.html')

@app.route("/signin")
def signin():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form["password"]
        if (db.find_one({"email": email, "password": password})):
            return render_template('signin.html')
        else:
            return "Return Invalid credentials"
    return render_template('signin.html');

if __name__ == '__main__':
    app.run(debug=True)
