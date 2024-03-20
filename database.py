from sqlalchemy import create_engine,text
import mysql.connector
from mysql.connector import Error

engine = create_engine("mysql+pymysql://root:Applem2air@127.0.0.1:3306/Project_manager?charset=utf8mb4")

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

def execute_query(query,connection=db_conn):
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        return "Query ran successfully..."
    except Error as e:
        return f"Error:{e}"

def load_dept_id():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Department;"))
        did = []
        for i in result:
            did.append(i)
        return did

def load_project():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Project;"))
        project = []
        for i in result:
            project.append(i)
        return project

def load_team():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Team;"))
        project = []
        for i in result:
            project.append(i)
        return project

def load_team_info():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Team_info;"))
        project = []
        for i in result:
            project.append(i)
        return project

def load_task():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Task_assigned;"))
        project = []
        for i in result:
            project.append(i)
        return project

def add_proj_to_db(projs):
    query = f"INSERT INTO Project VALUES({int(projs['projectID'])},'{projs['projectName']}','{projs['Description']}','{projs['startDate']}','{projs['endDate']}',{int(projs['deptID'])},'{projs['status']}');"
    try:
        execute_query(query)
    except Error as e:
        return f"Error:{e}"

def remove_from_proj(proj_id):
    query = f"DELETE FROM Project WHERE Proj_id={proj_id };"
    try:
        execute_query(query)
    except Error as e:
        return f"Error:{e}"
            
if __name__=='__main__':
    with engine.connect() as conn:
        result = conn.execute(text("select * from Department;"))
        for i in result:
            print(i)