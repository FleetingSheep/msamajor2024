from datetime import datetime
from student import Student
'''
function to write error log file
input: error message
output: none
'''

def write_to_error_log(error_message):
    try:
        log_file = open("error_log.txt", "w")
        log_file.write(f"{datetime.now()}, {error_message}\n\n")
        log_file.close()
    except Exception as e:
        print(e)
        return


students_list = []
student_file = open("students.csv")


def create_student_dict(students_list):
    student_dict_list = []
    for student in students_list:

        student_dict = {

            "first_name": student._fname,
            "last_name": student._lname,
            "major": student._major,
            "credit_hours": student._ch,
            "gpa": student._gpa,
            "id" : student._id,
            "class" : student._class
        }
        student_dict_list.append(student_dict)

    return student_dict_list


def get_students():

    for line_number, line in enumerate(student_file): #error handling
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
    return students_list

def get_student_dicts():
    
    students_list = get_students()
    student_dicts = create_student_dict(students_list)
    return student_dicts

