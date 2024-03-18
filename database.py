from sqlalchemy import create_engine,text


engine = create_engine("mysql+pymysql://root:Applem2air@127.0.0.1:3306/Project_manager?charset=utf8mb4")


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
    with engine.connect() as conn:
        query = text(f"INSERT INTO Project VALUES({int(projs['projectID'])},'{projs['projectName']}','{projs['Description']}','{projs['startDate']}','{projs['endDate']}',{int(projs['deptID'])},'{projs['status']}')")
        try:
            conn.execute(query)
            return "Success"
        except Exception as e:
            return f"{e}"

def remove_from_proj(proj_id):
    with engine.connect() as conn:
        query = text(f"Delete from Project where Proj_id={proj_id}")
        try:
            conn.execute(query)
            return "Success"
        except Exception as e:
            return f"{e}"
            
if __name__=='__main__':
    with engine.connect() as conn:
        result = conn.execute(text("select * from Department;"))
        for i in result:
            print(i)