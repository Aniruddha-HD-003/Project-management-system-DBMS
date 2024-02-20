from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/signin")
def signin():
    return render_template('sign.html')

if __name__=="__main__":
    app.run(debug=True)