from flask import Flask,render_template
from database import engine
from sqlalchemy import text

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/signin")
def signin():
    return render_template('sign.html') 

@app.route('/createnew')
def create():
    return render_template('createnew.html')

def load_dept_id():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Department;"))
        did = []
        for i in result:
            did.append(i)
        return did


@app.route('/info')
def inform():
    did = load_dept_id()
    return render_template('info.html',did = did)

@app.route('/projecttable')
def project():
    return render_template('projecttable.html')

@app.route('/uploadoc')
def uploadoc():
    return render_template('uploadoc.html')

@app.route('/signin2')
def signin2():
    return render_template('signin.html')

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
    return render_template('departmentdeets.html')



if __name__=="__main__":
    app.run(debug=True)
