students = []

# "self" is a self-reference to the object
class Student:

    school_name = "Springfield Elementary"

    def __init__(self, name, last_name, student_id=332):
        # The object name is the name passed in the init args
        self.name = name
        # Same with the ID
        self.student_id = student_id
        # And also the last name
        self.last_name = last_name
        # Append it to the student list
        students.append(self)

    # If someone tries to just print the object, return this instead
    def __str__(self):
        return "Student: " + self.name

    # A method to return just the name property of the student object, capitalized
    def get_name_capitalize(self):
        return self.name.capitalize() + " " + self.last_name.capitalize()

    def get_school_name(self):
        return self.school_name