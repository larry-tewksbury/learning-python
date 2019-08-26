# Reads a CSV "students.txt" and prints it out to the
import csv
from hs_student import HighSchoolStudent

student_list = []

def read_students():
    with open('students.txt', newline='') as student_csv:
        student_reader = csv.reader(student_csv, delimiter=',')
        for row in student_reader:
            # print(row)
            student = HighSchoolStudent(row[0],row[1],row[2])
            student_list.append(student.get_name_capitalize())
    return student_list

# read_students()