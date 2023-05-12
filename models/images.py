from models import common
import random

def convert_to_dictionary(item):
    return {"id": str(item[0]), "img_url": item[1], "text_desc": item[2], "img_year": item[3]}

def get_image(img_year):
    num_entries = common.sql_read("SELECT COUNT(img_year) FROM images WHERE img_year=%s", [img_year])[0][0]
    random_num =random.randint(0, num_entries-1)
    item = common.sql_read("SELECT * FROM images WHERE img_year=%s", [img_year])[random_num]
    return convert_to_dictionary(item)

def get_all_images():
    images = common.sql_read("SELECT * FROM images")
    return [convert_to_dictionary(image) for image in images]

def add_image(img_url, text_desc, img_year):
    common.sql_write("INSERT INTO images(img_url, text_desc, img_year) VALUES (%s, %s, %s);", [img_url, text_desc, img_year])

def get_image_id(id):
    item = common.sql_read("SELECT * FROM images WHERE id=%s", [id])[0]
    return convert_to_dictionary(item)

def edit_image(id, img_url, text_desc, img_year):
    common.sql_write(f"UPDATE images SET img_url=%s, text_desc=%s, img_year=%s WHERE id={id}", [img_url, text_desc, img_year])
    return

def delete_image(id):
    common.sql_write(f"DELETE FROM images WHERE id={id}", [id])