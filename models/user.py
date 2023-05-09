from flask import redirect, render_template, session
from models import common

def get_user(filter_clause, params):
  results = common.sql_read(f"SELECT * FROM users {filter_clause};", params)
  if len(results):
    user = results[0]
    return { "id": user[0], "username": user[1], "user_pwd": user[2] }
  return None
