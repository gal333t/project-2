import bcrypt
from models import common

def get_valid_user(username, plain_text_password):
  results = common.sql_read(f"SELECT * FROM users WHERE username=%s;", [username])
  if len(results):
    user = results[0]
    user_formatted = { "id": user[0], "username": user[1], "password_hash": user[2]}
    if bcrypt.checkpw(plain_text_password.encode(), user_formatted["password_hash"].encode()):
      return user_formatted
    return None
  return None

def add_user(username, plain_text_password):
  password_hash = bcrypt.hashpw(plain_text_password.encode(), bcrypt.gensalt()).decode()
  common.sql_write("INSERT INTO users (username, password_hash) VALUES (%s, %s);", [username, password_hash])