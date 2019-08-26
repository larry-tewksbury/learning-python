from flask import Flask
app = Flask(__name__)
from read_students import read_students

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/list-students")
def return_students():
    students = []
    students = read_students()
    return '\n'.join(students)

if __name__ == "__main__":
    app.run()