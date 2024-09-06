import sqlite3

db_name = "blog.db"
connection = None
cursor = None

def open():
    global connection, cursor
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()



def close():
    cursor.close()
    connection.close()

def get_categories():
    open()
    cursor.execute("SELECT * FROM category")
    res = cursor.fetchall()
    close()
    return res

def get_posts():
    open()
    cursor.execute("SELECT * FROM post")
    res = cursor.fetchall()
    close()
    return res

def get_posts_by_category(category_id):
    open()
    cursor.execute("SELECT * FROM post WHERE category_id = ?;", [category_id])
    res = cursor.fetchall()
    close()
    return res
