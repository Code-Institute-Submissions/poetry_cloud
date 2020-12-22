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
    poems = list(mongo.db.poems.find())
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
        return redirect(url_for("profile", username=session["user"]))
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
                    return redirect(url_for(
                        "profile", username=session["user"]))
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


# Profile function
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # retrieve the username from db which belongs to the session user
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # if session user is true then render appropriate profile or redirect to login
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# Logout function
@app.route("/logout")
def logout():
    # remove the session cookie for 'user' and redirect to login
    flash("You have successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))

# Add Poem function
@app.route("/add_poem", methods=["GET", "POST"])
def add_poem():
    if request.method == "POST":
        poem = {
            "type_name": request.form.get("type_name"),
            "poem_title": request.form.get("poem_title"),
            "poem_author": request.form.get("poem_author"),
            "poem_text": request.form.get("poem_text"),
            "created_by": session["user"]
        }
        mongo.db.poems.insert_one(poem)
        flash("Poem Successfully Added")
        return redirect(url_for("get_poems"))

    types = mongo.db.types.find().sort("type_name", 1)
    return render_template("add_poem.html", types=types)

# Edit poem function
# Search for the poem in the db with the poem id
# then update that poem with data from submit dictionary
# and display a message return user to edit page
@app.route("/edit_poem/<poem_id>", methods=["GET", "POST"])
def edit_poem(poem_id):
    if request.method == "POST":
        submit = {
            "type_name": request.form.get("type_name"),
            "poem_title": request.form.get("poem_title"),
            "poem_author": request.form.get("poem_author"),
            "poem_text": request.form.get("poem_text"),
            "created_by": session["user"]
        }
        mongo.db.poems.update({"_id": ObjectId(poem_id)}, submit)
        flash("Poem Successfully Updated")

    poem = mongo.db.poems.find_one({"_id": ObjectId(poem_id)})
    types = mongo.db.types.find().sort("type_name", 1)
    return render_template("edit_poem.html", poem=poem, types=types)

# Delete poem function
# Search for the poem in the db with the poem id
# then remove from db, flash message to user,
# return user to home page
@app.route("/delete_poem/<poem_id>")
def delete_poem(poem_id):
    mongo.db.poems.remove({"_id": ObjectId(poem_id)})
    flash("Poem Successfully Deleted")
    return redirect(url_for("get_poems"))


# Get types function
# Gets types from the db, converts to a list and returns to our types template
@app.route("/get_types")
def get_types():
    types = list(mongo.db.types.find().sort("type_name", 1))
    return render_template("types.html", types=types)

# Add type function
# If the add_type function is called using the 'POST' method 
# then we'll get the data from the form and insert into db
# Otherwise, default 'GET' method will render the empty 'Add Type' form
@app.route("/add_type", methods=["GET", "POST"])
def add_type():
    if request.method == "POST":
        type = {
            "type_name": request.form.get("type_name")
        }
        mongo.db.types.insert_one(type)
        flash("New Poem Type Added")
        return redirect(url_for("get_types"))

    return render_template("add_type.html")


# how and where to run the application.
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
