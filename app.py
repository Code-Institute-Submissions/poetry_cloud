import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# the @app.route decorator is used to bind the URL to the get_poems function.
# as a result, when the user visits the URL, the output of the function will
# render in the browser.
@app.route("/")
@app.route("/get_poems")
def get_poems():
    poems = mongo.db.poems.find()
    return render_template("poems.html", poems=poems)


# Register function
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Verify if the username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("That username is already in use, please choose another.")
            return redirect(url_for("register"))
        # Gets the details from the register form
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        # Inserts the user into the users collection
        mongo.db.users.insert_one(register)

        # Place the newly created user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("You have successfully registered!")
    return render_template("register.html")


# Login function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # if request method equals POST, check if username is found in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # then check if the hashed password matches the one the user submitted
            # if true, then we can log the user in and display a welcome message
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
            else:
                # if the password doesn't match, flash message and redirect to login
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # if there wasn't a match for the existing_user variable,
            # display message and redirect to login and try again
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# how and where to run the application.
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
