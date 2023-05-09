import psycopg2
from models import common

def insert_message(user_msg):
    common.sql_write("INSERT INTO messages (user_msg) VALUES (%s);", [user_msg])

def get_message(id):
    common.sql_read("SELECT * FROM messages WHERE id=%s", [id])[0]

def edit_message(id, user_msg):
    common.sql_write(f"UPDATE messages SET user_msg=%s WHERE id={id}", [user_msg])

def delete_message(id):
    common.sql_write(f"DELETE FROM messages WHERE id={id}", [id])