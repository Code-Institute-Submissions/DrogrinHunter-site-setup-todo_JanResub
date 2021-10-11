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


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checking whether a user has an account
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # this section checks to ensure that the
            # password entered matches DB
            if check_password_hash(existing_user["password"],
                request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for("profile",
                        username=session["user"]))
            else:
                # invalid password
                flash("Invalid Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username does not exist
            flash("Invalid username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/get_tasks")
def get_tasks():
    if "user" in session.keys() == True:
        tasks = list(mongo.db.tasks.find())
        return render_template("tasks.html", tasks=tasks)
    return redirect(url_for("login"))


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    return render_template("tasks.html", tasks=tasks)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # checking to see if the username is already taken by another user
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("This username already exists, please choose another")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # putting the new user into the 'session' cookie
        # that is stored in the local storage
        session["user"] = request.form.get("username").lower()
        flash("Registration has been successful")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # this takes the session user's username from the db
    username_mongo = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if username == username_mongo:
        tasks = list(mongo.db.tasks.find({
            "created_by": username_mongo
        }))
        return render_template("profile.html", username=username, tasks=tasks)

    session.pop("user")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have logged out successfully")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
        if request.method == "POST":
            is_urgent = "on" if request.form.get("is_urgent") else "off"
            task = {
                "site_name": request.form.get("site_name"),
                "task_name": request.form.get("task_name"),
                "task_description": request.form.get("task_description"),
                "is_urgent": is_urgent,
                "due_date": request.form.get("due_date"),
                "created_by": session["user"]

            }
            mongo.db.tasks.insert_one(task)
            flash("Task Has Been Successfully Added")
            return redirect(url_for("get_tasks"))

        site_name = mongo.db.location.find().sort("site_name", 1)
        return render_template("add_task.html", site_name=site_name)


@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = {
            "site_name": request.form.get("site_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit)
        flash("Task Has Been Successfully Updated")

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    site_name = mongo.db.location.find().sort("site_name", 1)
    return render_template("edit_task.html", task=task, site_name=site_name)


@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_tasks"))


@app.route("/locations")
def locations():
    if "user" in session.keys() == True:
        locations = list(mongo.db.location.find().sort("site_name", 1))
        return render_template("locations.html", location=locations)

    return redirect(url_for("login"))


@app.route("/add_site", methods=["GET", "POST"])
def add_site():
    if "user" in session.keys() == True:
        if request.method == "POST":
            location = {
                "site_name": request.form.get("site_name")
            }
            mongo.db.location.insert_one(location)
            flash("New Location Added")
            return redirect(url_for("locations"))
        return render_template("add_site.html")

    return redirect(url_for("login"))


@app.route("/edit_site/<site_id>", methods=["GET", "POST"])
def edit_site(site_id):
    if request.method == "POST":
        submit = {
            "site_name": request.form.get("site_name")
        }
        mongo.db.location.update({"_id": ObjectId(site_id)}, submit)
        flash("Location Successfully Updated")
        return redirect(url_for("locations"))

    locations = mongo.db.location.find_one({"_id": ObjectId(site_id)})
    return render_template("edit_site.html", location=locations)


@app.route("/delete_site/<site_id>")
def delete_site(site_id):
    mongo.db.location.remove({"_id": ObjectId(site_id)})
    flash("Location Successfully Removed")
    return redirect(url_for("locations"))


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# change debug to false once completed
