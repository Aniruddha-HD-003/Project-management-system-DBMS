from flask import Flask,render_template
from database import engine
from sqlalchemy import text

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

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


@app.route('/info')
def inform():
    did = load_dept_id()
    return render_template('info.html',did = did)

@app.route('/projecttable')
def project():
    project = load_project()
    return render_template('projecttable.html', project=project)

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

@app.route('/inserttoproj')
def inserttoproj():
    return render_template('inserttoproj.html')

@app.route('/deleteproj')
def deleteproj():
    return render_template('deleteproj.html')

@app.route('/deletedep')
def deletedep():
    return render_template('deletedep.html')

@app.route('/depinsert')
def depinsert():
    return render_template('depinsert.html')

@app.route('/departmentdeets')
def dep():
    did=load_dept_id()
    return render_template('departmentdeets.html', did=did)



if __name__=="__main__":
    app.run(debug=True)
