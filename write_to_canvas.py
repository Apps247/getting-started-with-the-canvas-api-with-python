import dotenv
import os
import canvasapi

env_file = 'sample.env'
dotenv.load_dotenv(env_file)

TOKEN = os.environ.get('CANVAS_API_TOKEN')
BASEURL = 'https://ubc.instructure.com'

canvas_api = canvasapi.Canvas(BASEURL, TOKEN)

global course

def welcome_user():
    user = canvas_api.get_user('self')
    print(type(user))
    print("Welcome, " + user.name)

def load_course(course_id):
    # course id is Canvas course id in format of 123456
    global course
    course = canvas_api.get_course(course_id)
    print("Loaded course: " + course.name)


def get_lab_section(lab_section_code, term, course_code="CPSC 121"):
    """
    Args:
    - section (str): The section number.
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


welcome_user()
load_course(123413)
section = get_lab_section("L14", "2023W1")
lab = get_lab_assignment(2, "2023W1")
print(lab)


print(lab.get_submission(1083406).grade)
# print(lab.get_submission(1083406).delete())
# print(lab.get_submission(1083406).edit(submission={'grade': 2}))
print(lab.get_submission(1083406).edit(submission={'posted_grade': 3}))

# for student in section.get_enrollments():
#     print(student.user)
#     print(student.user['name'], student.user['id'])


# for student in section.get_users(enrollment_type=['student']):
#     print(student.name)
#     print(student.id)
    
