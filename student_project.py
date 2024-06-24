from datetime import datetime

'''
function to write error log file
input: error message
output: none
'''

def write_to_error_log(error_message):
    try:
        log_file = open("error_log.txt", "a")
        log_file.write(f"{datetime.now()}, {error_message}\n\n")
        log_file.close()
    except Exception as e:
        print(e)
        return


students_list = []
student_file = open("students.csv")

class Student:

    def __init__(self, fname, lname, major, ch, gpa, id):
        self._fname = fname
        self._lname = lname
        self._major = major
        self._ch = int(ch)
        self._gpa = gpa
        self._id = id
        self.get_class_level()

    def __str__(self):
        return f"{self._class} {self._fname} {self._lname}:\n\nMajor: {self._major}, Credit Hours: {self._ch}\nGPA: {self._gpa}, ID: {self._id}\n"

    def get_class_level(self):

        if self._ch > 90:
            self._class = "Senior"
        elif self._ch >= 61:
            self._class = "Junior"
        elif self._ch >= 31:
            self._class = "Sophomore"
        elif self._ch >= 0:
            self._class = "Freshman"

    def update_credit_hours(self, added_hours):
        self._ch += added_hours
        self.get_class_level()

def get_students():

    for line_number, line in enumerate(student_file):
        try:
            if line_number == 0:
                continue
            x = line.split(",")
            if len(x) > 6:
                write_to_error_log(f"Too many entries on line {line_number}")
                continue
            elif len(x) < 6:
                write_to_error_log(f"Too few entries on line {line_number}")
                continue
            else:
                x = Student(x[0], x[1], x[2], x[3], x[4], x[5])
                students_list.append(x)
        except:
            write_to_error_log(f"Unknown error on line {line_number}")
    for student in students_list:
        print(student)

def main():
    
    get_students()


main()