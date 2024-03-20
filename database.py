import mysql.connector
from mysql.connector import Error

def create_database_connection(host,user,pw,db_name):
    connection=None
    try:
        connection=mysql.connector.connect(
            host=host,
            user=user,
            passwd=pw,
            database=db_name
        )
        print("Database connection successful...")
    except Error as e:
        print(f"Error:{e}")
    return connection

db_conn = create_database_connection("localhost","root","Applem2air","Project_manager")

def read_table(query,connection=db_conn):
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        did = [i for i in result]
        return did
    except Error as e:
        return f"Error:{e}"

def execute_query(query,connection=db_conn):
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        return "Query ran successfully..."
    except Error as e:
        return f"Error:{e}"

            