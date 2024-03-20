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

@app.route('/task')
def task():
    return render_template('task.html')
@app.route('/taskinsert')
def taskinsert():
    return render_template('taskinsert.html')
@app.route('/taskdel')
def taskdel():
    return render_template('taskdel.html')
@app.route('/teams')
def teams():
    return render_template('teams.html')

@app.route('/teaminsert')
def teaminsrt():
    return render_template('teaminsert.html')

@app.route('/teamdel')
def teamdel():
    return render_template('teamdel.html')











if __name__=="__main__":
    app.run(debug=True)
