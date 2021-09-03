from mysql import connector

from database.connection import create_connection


def insert(data):
    conn = create_connection()
    sql = """INSERT INTO recipes (title, category, guide_url, budget, img_path,
                                    ingredients, directions)
            VALUES(%s, %s, %s, %s, %s, %s, %s)                        
            """
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert_recuoe function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()


def select_all():
    conn = create_connection()
    sql = """SELECT id, img_path, title, category FROM recipes"""
    try:
        cur = conn.cursor()
        cur.execute(sql)
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()


def select_by_id(_id):
    conn = create_connection()
    sql = f"""SELECT * FROM recipes WHERE id = {_id}"""
    try:
        cur = conn.cursor()
        cur.execute(sql)
        recipe = cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_id function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def update(_id, data):
    conn = create_connection()
    sql = f"""UPDATE recipes SET 
                                title = %s, 
                                category = %s, 
                                guide_url = %s, 
                                budget = %s, 
                                img_path = %s,
                                ingredients = %s, 
                                directions = %s
            WHERE id = {_id}                       
            """
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at update recipe function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()


def select_by_parameter(param):
    conn = create_connection()
    param = f"%{param}%"
    sql = """SELECT id, img_path, title, category FROM recipes
            WHERE title LIKE %s OR category LIKE %s
            """
           
    try:
        cur = conn.cursor()
        cur.execute(sql, (param, param))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()


def delete(_id):
    conn = create_connection()
    sql = f""" DELETE FROM recipes
            WHERE id = {_id}                       
            """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at delete recipe function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
