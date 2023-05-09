from flask import Flask, render_template, redirect, request, session
import os
import psycopg2
from models import messages

app = Flask(__name__)
app.config["SECRET_KEY"] = "My secret key"

@app.route("/")
def index():
    connection = psycopg2.connect(host=os.getenv("PGHOST", "dpg-ch8fge5gk4q7lmq3l460-a.oregon-postgres.render.com"),
    user=os.getenv("PGUSER", "pg"),
    password=os.getenv("PGPASSWORD", "pSyCdeo1JQVO7wzGZm2wCEUOUXb5Axo9"),
    port=os.getenv("PGPORT", "5432"),
    dbname=os.getenv("PGDATABASE", "project2_8x9r"))
    # connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM images;")
    results = cursor.fetchall()
    connection.close()
    return f"{results[0]}"

@app.route("/home")
def homepage():
    return render_template("home.html")

@app.route("/login")
def loginpage():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login_action():
    username = request.form.get("username")
    #TO DO CHECK PASSWORD
    curr_user = user.get_user("WHERE username=%s", [username])
    if curr_user:
        session["user_id"] = curr_user["id"]
        session["user_name"] = curr_user["user_name"]
        return redirect('/home')
    else:
        return render_template("login_error.html")

@app.route("/logout")
def logout():
    session["user_id"] = None
    session["user_name"] = None
    return redirect("/home")

@app.route("/messages")
def disp_messages():
    return render_template("messages.html")

@app.route("/forms/messages/add")
def add_message_form():
    # TODO add sessions in
    return render_template("add_message.html")

@app.route("/api/messages/add", methods=["POST"])
def add_message():
    form = request.form
    messages.insert_message(form.get("user_msg"))
    return redirect("/messages")

@app.route("/forms/messages/edit/<id>")
def edit_message_form(id):
    # TO DO add sessions in
    return render_template("edit_message.html", messages=messages.get_message(id))

@app.route("/api/messages/edit/<id>", methods=["POST"])
def edit_message(id):
    form = request.form
    messages.edit_message(id, form.get("user_msg"))
    return redirect("/messages")

@app.route("/forms/messages/delete")
def delete_message_form(id):
    # TO DO add sessions in
    return render_template("delete_message.html", messages=messages.get_message(id))

@app.route("/api/messages/delete", methods=["POST"])
def delete_message():
    # TO DO add in sql commands
    messages.delete_message(request.form.get("id"))    
    return redirect("/messages")

if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
