from models import common

def convert_to_dictionary(item):
    return {"id": str(item[0]), "user_msg": item[1]}

def insert_message(user_msg):
    common.sql_write("INSERT INTO messages (user_msg) VALUES (%s);", [user_msg])

def get_message(id):
    item = common.sql_read("SELECT * FROM messages WHERE id=%s", [id])[0]
    return convert_to_dictionary(item)

def get_all_messages():
    items = common.sql_read("SELECT * FROM messages;")
    return [convert_to_dictionary(item) for item in items]

def edit_message(id, user_msg):
    common.sql_write(f"UPDATE messages SET user_msg=%s WHERE id={id}", [user_msg])

def delete_message(id):
    common.sql_write(f"DELETE FROM messages WHERE id={id}", [id])