from flask import Flask, render_template, request
from student import Student

app = Flask(__name__)
    

class_roster = [Student('Andrew', 'Senior', 95), Student('Joe', 'Senior', 90),
                Student('Chris', 'Junior', 95), Student('Heather', 'Senior', 100),
                Student('Theo', 'Freshman', 90), Student('Eric', 'Junior', 90),
                Student('Isaac', 'Sophomore', 90)]

@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")

@app.route("/welcome/<string:student_name>")
def welcome(student_name):

    return render_template("welcome.html", student_name=student_name)

@app.route("/roster/<int:grade_view>")
def roster(grade_view):
    return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)

if __name__ == '__main__':
    app.run()