import psycopg2
from models import common

def insert_message(user_msg):
    common.sql_write("INSERT INTO messages (user_msg) VALUES (%s);", [user_msg])
