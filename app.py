from flask import Flask, render_template, redirect, request, session
import os
import psycopg2
import bcrypt
from models import messages, images, user

app = Flask(__name__)
app.config["SECRET_KEY"] = "My secret key"

@app.route("/")
def index():
    if session.get("user_id"):
        return render_template("home.html")
    else:
        return redirect("/login")

@app.route("/login")
def loginpage():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_action():
    username = request.form.get("username")
    plain_text_password = request.form.get("password")
    curr_user = user.get_valid_user(username, plain_text_password)
    if curr_user:
        session["user_id"] = curr_user["id"]
        session["username"] = curr_user["username"]
        return redirect("/")
    else:
        return render_template("login_error.html")

@app.route("/logout")
def logout():
    session["user_id"] = None
    session["username"] = None
    return redirect("/")

@app.route("/new-user")
def newuser():
    return render_template("new_user.html")

@app.route("/new-user", methods=["POST"])
def newuser_action():
    user.add_user(request.form.get("username"), request.form.get("password"))
    return redirect("/login")    

@app.route("/messages")
def disp_messages():
    if session.get("user_id"):
        return render_template("messages.html", messages=messages.get_all_messages())   
    else:
        return redirect("/login")
            
@app.route("/forms/messages/add")
def add_message_form():
    if session.get("user_id"):
        return render_template("add_message.html")
    else:
        return redirect("/login")

@app.route("/api/messages/add", methods=["POST"])
def add_message():
    form = request.form
    messages.insert_message(form.get("user_msg"), form.get("username"))
    return redirect("/messages")

@app.route("/forms/messages/edit/<id>")
def edit_message_form(id):
    if session.get("user_id"):
        return render_template("edit_message.html", messages=messages.get_message(id))
    else:
        return redirect("/login")    

@app.route("/api/messages/edit/<id>", methods=["POST"])
def edit_message(id):
    form = request.form
    messages.edit_message(id, form.get("user_msg"))
    return redirect("/messages")

@app.route("/forms/messages/delete/<id>")
def delete_message_form(id):
    if session.get("user_id"):
        return render_template("delete_message.html", messages=messages.get_message(id))
    else:
        return redirect("/login")   

@app.route("/api/messages/delete", methods=["POST"])
def delete_message():
    messages.delete_message(request.form.get("id"))    
    return redirect("/messages")

@app.route("/message-actions")
def message_actions():
    if session.get("user_id"):
        return render_template("message-actions.html")
    else:
        return redirect("/login")

@app.route("/img-search")
def img_search():
    if session.get("user_id"):
        return render_template("img_search.html")
    else:
        return redirect("/login")

@app.route("/img-display", methods=["POST"])
def img_display():
    form = request.form
    return render_template("img_display.html", images= images.get_image(form.get("img_year")))

if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
