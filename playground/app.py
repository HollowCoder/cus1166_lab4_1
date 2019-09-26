from flask import Flask, render_template, request
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class_roster = [('Andrew', 'Senior', '95'), ('Joe', 'Senior', '90'),
                ('Chris', 'Junior', '95'), ('Heather', 'Senior', '100'),
                ('Theo', 'Freshman', '90'), ('Eric', 'Junior', '90'),
                ('Isaac', 'Sophomore', '90')]

@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")

@app.route("/welcome/<string:student_name>")
def welcome():

    return render_template("welcome.html", student_name=student_name)

@app.route("/roster/<int:grade_view>")
def roster():
    return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)