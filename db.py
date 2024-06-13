import mysql.connector
from mysql.connector import Error

# Configuración de la base de datos directamente en el script
DB_CONFIG = {
    "host": "localhost",
    "user": "adminps",
    "passwd": "adminps",
    "database": "petShop"
}

def crear_conexion():
    connection = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        print("Conexión a la base de datos exitosa")
    except Error as e:
        print(f"El error '{e}' ocurrió")
    return connection


def execute_query(query, params=None):
    connection = crear_conexion()
    if connection is None:
        return

    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print("Consulta ejecutada con éxito")
    except Error as e:
        print(f"El error '{e}' ocurrió")
    finally:
        cursor.close()
        connection.close()


def fetch_query(query, params=None):
    connection = crear_conexion()
    if connection is None:
        return None

    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query, params)
        result = cursor.fetchall()
    except Error as e:
        print(f"El error '{e}' ocurrió")
    finally:
        cursor.close()
        connection.close()
    return result


def ultimoid(query, params=None):
    connection = crear_conexion()
    if connection is None:
        return None

    cursor = connection.cursor()
    last_id = None
    try:
        cursor.execute(query, params)
        connection.commit()
        last_id = cursor.lastrowid
        print("Consulta ejecutada con éxito")
    except Error as e:
        print(f"El error '{e}' ocurrió")
    finally:
        cursor.close()
        connection.close()
    return last_id
