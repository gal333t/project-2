from models import common

def convert_to_dictionary(item):
    return {"id": str(item[0]), "img_url": item[1], "text_desc": item[2], "img_year": item[3]}

def get_image(img_year):
    item = common.sql_read("SELECT * FROM images WHERE img_year=%s", [img_year])[0]
    return convert_to_dictionary(item)