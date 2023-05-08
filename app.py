from flask import Flask, render_template
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    # connection = psycopg2.connect(host=os.getenv("PGHOST"), user=os.getenv("PGUSER"), password=os.getenv("PGPASSWORD"), port=os.getenv("PGPORT"), dbname=os.getenv("PGDATABASE"))
    connection = psycopg2.connect(os.getenv("postgres://pg:pSyCdeo1JQVO7wzGZm2wCEUOUXb5Axo9@dpg-ch8fge5gk4q7lmq3l460-a.oregon-postgres.render.com/project2_8x9r"))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mytable;")
    results = cursor.fetchall()
    connection.close()
    return f"{results[0]}"

@app.route('/home')
def homepage():
    return render_template("home.html")

@app.route('/messages')
def messages():
    return render_template("messages.html")

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
