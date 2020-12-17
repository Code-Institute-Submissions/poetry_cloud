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

# Here, the @app.route decorator is used to bind the URL to the get_poems function.
# As a result, when the user visits the URL, the output of the function will render in the browser.
@app.route("/")
@app.route("/get_poems")
def get_poems():
    poems = mongo.db.poems.find()
    return render_template("poems.html", poems=poems)


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


# How and where to run the application.
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
