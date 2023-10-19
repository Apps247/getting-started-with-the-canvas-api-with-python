import dotenv
import os
import canvasapi

env_file = 'sample.env'
dotenv.load_dotenv(env_file)

log_file = open('log.txt', 'w')


TOKEN = os.environ.get('CANVAS_API_TOKEN')
BASEURL = 'https://ubc.instructure.com'

canvas_api = canvasapi.Canvas(BASEURL, TOKEN)

global course

def welcome_user():
    user = canvas_api.get_user('self')
    print("Welcome, " + user.name)

def load_course(course_id):
    # course id is Canvas course id in format of 123456
    global course
    course = canvas_api.get_course(course_id)
    print("Course: " + course.name)


def get_lab_section(lab_section_code, term, course_code="CPSC 121"):
    """
    Args:
    - section (str): The section number, (e.g. L1C).
    - term (str): The term in the format of YYYYT# (e.g. 2023W1).
    - course_code (str): The course code (default is "CPSC 121").
    """
    for section in course.get_sections():
        if str(section.name) == " ".join([course_code, lab_section_code, term]):
            return section
        
def get_lab_assignment(lab_no, term, course_code="CPSC 121"):
    """
    Args:
    - lab_no (int): The lab number.
    - term (str): The term in the format of YYYYT# (e.g. 2023W1).
    - course_code (str): The course code (default is "CPSC 121").
    """
    for assignment in course.get_assignments():
        lab_no = str(lab_no)
        if len(lab_no) == 1:
            lab_no = "0" + lab_no
        if str(assignment.name) == "Lab " + lab_no:
            return assignment
        
def get_students(section):
    """Gets the students in a lab section with their Canvas user id and name.
    
    Keyword arguments:
    section -- Canvas section object
    lab -- Canvas assignment object

    Returns: list of Canvas enrollment objects which can be indexed for 'name' or 'id'
    """
    
    return [enrollment for enrollment in section.get_enrollments() if enrollment.type == "StudentEnrollment"]

def update_grades(lab, section, student_grades):
    """Updates the grades of students in a lab section.
    
    Keyword arguments:
    lab -- Canvas assignment object
    student_grades -- dictionary of student names and their corresponding total marks for the lab
    """
    
    log("Retrieved grades from Excel:")
    for student in student_grades:
        log("Student: " + student + ", Grade: " + str(student_grades[student]))

    log("Writing to Canvas...")
    for student in get_students(section):
        if student.user['name'] in student_grades:
            grade = student_grades[student.user['name']]
            if grade is None:
                log(f"No grade available for {student.user['name']} in Excel Sheet")
            else:
                if lab.get_submission(student.user['id']).grade is not None:
                    log(f"{student.user['name']} is already graded")
                else:
                    lab.get_submission(student.user['id']).edit(submission={'posted_grade': grade})
                    log(f"Updated {student.user['name']}'s grade to {grade}.", silent=True)
        else:
            log(f"{student.user['name']} not found in Excel Sheet")
    log("Operation completed")


def log(message, silent=False):
    log_file.write(message + "\n")
    if not silent:
        print(message)


if __name__ == "__main__":
    welcome_user()
    load_course(123413)
    section = get_lab_section("L14", "2023W1")
    lab = get_lab_assignment(2, "2023W1")
    print(lab)
    for student in get_students(section):
        print(student.user)


# print(lab.get_submission(1083406).grade)
# print(lab.get_submission(1083406).delete())
# print(lab.get_submission(1083406).edit(submission={'grade': 2}))
# print(lab.get_submission(1083406).edit(submission={'posted_grade': 3}))

# for student in section.get_enrollments():
#     print(student.user)
#     print(student.user['name'], student.user['id'])


# for student in section.get_users(enrollment_type=['student']):
#     print(student.name)
#     print(student.id)
    
