from flask import Flask,render_template, jsonify, request
import database as db

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/info')
def inform():
    return render_template('info.html')

@app.route('/departmentdeets')
def dep():
    query = "SELECT * FROM Department;"
    did = db.read_table(query=query)
    return render_template('departmentdeets.html', did=did)

@app.route('/departmentdeets/depinsert')
def depinsert():
    return render_template('depinsert.html')

@app.route('/depinsert/insert', methods=['post'])
def insert_dept():
    data = request.form
    dept = dict(data)
    query = f"INSERT INTO Department VALUES({dept['deptID']},'{dept['deptName']}');"
    status=db.execute_query(query=query)
    return status

@app.route('/departmentdeets/deletedep')
def deletedep():
    return render_template('deletedep.html')

@app.route('/deletedep/delete', methods=['post'])
def delete_dept():
    data = request.form
    id = (dict(data))['deptID']
    query = f"DELETE FROM Department WHERE Dept_id={id};"
    status=db.execute_query(query=query)
    return status

@app.route('/projecttable')
def project():
    query = "SELECT * FROM Project;"
    project = db.read_table(query=query)
    return render_template('projecttable.html', project=project)

@app.route('/projecttable/inserttoproj')
def inserttoproj():
    return render_template('inserttoproj.html')

@app.route('/inserttoproj/insert', methods=['post'])
def insert_proj():
    data = request.form
    projs = dict(data)
    query = f"INSERT INTO Project VALUES({int(projs['projectID'])},'{projs['projectName']}','{projs['Description']}','{projs['startDate']}','{projs['endDate']}',{int(projs['deptID'])},'{projs['status']}');"
    status=db.execute_query(query=query)
    return status

@app.route('/projecttable/deleteproj')
def deleteproj():
    return render_template('deleteproj.html')

@app.route('/deleteproj/delete', methods=['post'])
def delete_proj():
    data = request.form
    id = (dict(data))['projectID']
    query = f"DELETE FROM Project WHERE Proj_id={id};"
    status=db.execute_query(query=query)
    return status

@app.route('/teams')
def teams():
    query = "SELECT * FROM Team;"
    teams = db.read_table(query=query)
    return render_template('teams.html',teams=teams)

@app.route('/teams/teaminsert')
def teaminsrt():
    return render_template('teaminsert.html')

@app.route('/teaminsert/insert', methods=['post'])
def insert_team():
    data = request.form
    teams = dict(data)
    query = f"INSERT INTO Team VALUES({teams['tid']},'{teams['tname']}',{teams['pid']});"
    status=db.execute_query(query=query)
    return status

@app.route('/teams/teamdel')
def teamdel():
    return render_template('teamdel.html')

@app.route('/teamdel/delete', methods=['post'])
def delete_team():
    data = request.form
    id = (dict(data))['tid']
    query = f"DELETE FROM Team WHERE Team_id={id};"
    status=db.execute_query(query=query)
    return status

@app.route('/teammate')
def teammates():
    query = "SELECT * FROM Team_members;"
    teammate = db.read_table(query=query)
    return render_template('teammate.html',teammate=teammate)

@app.route('/teammate/teamminsert')
def teamminsrt():
    return render_template('teamminsert.html')

@app.route('/teamminsert/insert', methods=['post'])
def insert_teammate():
    data = request.form
    teammates = dict(data)
    query = f"INSERT INTO Team_members VALUES({teammates['tid']},'{teammates['mname']}','{teammates['usn']}');"
    status=db.execute_query(query=query)
    return status

@app.route('/teammate/teammdel')
def teammdel():
    return render_template('teammdel.html')

@app.route('/teammdel/delete', methods=['post'])
def delete_temmate():
    data = request.form
    usn = (dict(data))['usn']
    query = f"DELETE FROM Team_members WHERE USN='{usn}';"
    status=db.execute_query(query=query)
    return status

@app.route('/task')
def task():
    query = "SELECT * FROM Task_assigned;"
    tasks = db.read_table(query=query)
    return render_template('task.html', tasks=tasks)

@app.route('/task/taskinsert')
def taskinsert():
    return render_template('taskinsert.html')

@app.route('/taskinsert/insert', methods=['post'])
def insert_task():
    data = request.form
    tasks = dict(data)
    query = f"INSERT INTO Task_assigned VALUES('{tasks['usn']}',{tasks['tid']},'{tasks['task']}');"
    status=db.execute_query(query=query)
    return status

@app.route('/task/taskdel')
def taskdel():
    return render_template('taskdel.html')

@app.route('/taskdel/delete', methods=['post'])
def delete_task():
    data = request.form
    usn = (dict(data))['usn']
    query = f"DELETE FROM Task_assigned WHERE USN='{usn}';"
    status=db.execute_query(query=query)
    return status


if __name__=="__main__":
    app.run(debug=True)
