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

if __name__=="__main__":
    app.run(debug=True)
