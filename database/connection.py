from mysql import connector


config = {
    'user': 'root',
    'password': 'Admin1234',
    'host': 'localhost',
    'database': 'recipes_db'
}

def create_connection():
    conn = None
    try:
        conn = connector.connect(**config)
    except connector.Error as err:
        print(f"Error at create_connection function: {err.msg}" )
    return conn