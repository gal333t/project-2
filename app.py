from flask import Flask, render_template
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    # connection = psycopg2.connect(host=os.getenv("PGHOST", "dpg-ch8fge5gk4q7lmq3l460-a.oregon-postgres.render.com"),
    # user=os.getenv("PGUSER", "pg"),
    # password=os.getenv("PGPASSWORD", "INSERTHERE"),
    # port=os.getenv("PGPORT", "5432"),
    # dbname=os.getenv("PGDATABASE", "project2_8x9r"))
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM images;")
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
