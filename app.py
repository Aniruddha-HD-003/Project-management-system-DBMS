from flask import Flask,render_template

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


@app.route('/info')
def inform():
    return render_template('info.html')

if __name__=="__main__":
    app.run(debug=True)


@app.route('/projecttable')
def inform():
    return render_template('projecttable.html')

if __name__=="__main__":
    app.run(debug=True)
