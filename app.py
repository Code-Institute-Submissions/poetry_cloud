""" I borrowed code from the Code Institute's Task Manager Mini Project
and appropriated to help with the below CRUD functions
and authentication functionality.
"""

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

# The @app.route decorator is used to bind the URL to the get_poems function.
# As a result, when the user visits the URL,
# the output of the function will render in the browser.


@app.route("/")
@app.route("/get_poems")
def get_poems():
    poems = list(mongo.db.poems.find())
    return render_template("poems.html", poems=poems)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    poems = list(mongo.db.poems.find({"$text": {"$search": query}}))
    return render_template("poems.html", poems=poems)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Verify if the username already exists in the database.
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("That username is already in use, please choose another.")
            return redirect(url_for("register"))
        # Gets the details from the register form.
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        # Inserts the user into the users collection.
        mongo.db.users.insert_one(register)

        # Place the newly created user into session cookie.
        session["user"] = request.form.get("username").lower()
        flash("You have successfully registered!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # If request method equals POST, check if username
        # is found in the db.
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Then check if the hashed password matches the one the user
            # submitted if true, log the user in and display a welcome message.
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # If the password doesn't match,
                # flash message and redirect to login.
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # If there wasn't a match for the existing_user variable,
            # display message and redirect to login and try again.
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Retrieve the username from db which belongs to the session user.
    # Find poems created by the user then render to appropriate profile or
    # redirect to login if unsuccessful.

    try:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        poems = mongo.db.poems.find({"created_by": session["user"]})
        return render_template("profile.html", username=username, poems=poems)
    except KeyError:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove the session cookie for 'user' and redirect to login.
    flash("You have successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


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
        return redirect(url_for('profile', username=session['user']))

    types = mongo.db.types.find().sort("type_name", 1)
    return render_template("add_poem.html", types=types)


@app.route("/edit_poem/<poem_id>", methods=["GET", "POST"])
def edit_poem(poem_id):
    # Search for the poem in the db with the poem id.
    # Then update that poem with data from submit dictionary
    # and display a message. Return user to edit page.
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


@app.route("/delete_poem/<poem_id>")
def delete_poem(poem_id):
    # Search for the poem in the db with the poem id.
    # Then remove from db, flash message to user and
    # return user to home page
    mongo.db.poems.remove({"_id": ObjectId(poem_id)})
    flash("Poem Successfully Deleted")
    return redirect(url_for("get_poems"))


@app.route("/get_types")
def get_types():
    # Gets types from the db, converts to a list and
    # returns to types template.

    types = list(mongo.db.types.find().sort("type_name", 1))
    return render_template("types.html", types=types)


@app.route("/add_type", methods=["GET", "POST"])
def add_type():
    # If add_type function is called using the 'POST' method
    # then get the data from the form and insert into db
    # Otherwise, default 'GET' method will render the empty 'Add Type' form.
    if request.method == "POST":
        type = {
            "type_name": request.form.get("type_name")
        }
        mongo.db.types.insert_one(type)
        flash("New Poem Type Added")
        return redirect(url_for("get_types"))

    return render_template("add_type.html")


@app.route("/edit_type/<type_id>", methods=["GET", "POST"])
def edit_type(type_id):
    # If the request method equals 'POST', submit the edited type from the form
    # Then use the update method on the types collection.
    # Once updated, redirect the admin back to get_types view.

    if request.method == "POST":
        submit = {
            "type_name": request.form.get("type_name")
        }
        mongo.db.types.update({"_id": ObjectId(type_id)}, submit)
        flash("Poem Type Successfully Updated")
        return redirect(url_for("get_types"))

    type = mongo.db.types.find_one({"_id": ObjectId(type_id)})
    return render_template("edit_type.html", type=type)


@app.route("/delete_type/<type_id>")
def delete_type(type_id):
    # Use the remove method on the types collection in MongoDB to delete type.
    # Once deleted, display flash message to admin user.
    # Redirect admin user back to all available types.

    mongo.db.types.remove({"_id": ObjectId(type_id)})
    flash("Poem Type Successfully Deleted")
    return redirect(url_for("get_types"))


@app.errorhandler(404)
def page_not_found(e):
    # Custom 404 error page will display if user types incorrect url
    # or url does not exist.
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    # Custom 500 Internal server error page will display if the app fails.
    return render_template('500.html'), 500


# How and where to run the application.
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
