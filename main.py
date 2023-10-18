from read_excel import read_excel
from write_to_canvas import *



lab_no = 3
lab_no_spoof = 9
section_name = "L14"
term = "2023W1"
cpsc_121 = 123413

student_grades = read_excel(f'{section_name}.xlsx', lab_no=lab_no)
welcome_user()
load_course(cpsc_121)
section = get_lab_section(section_name, term)
lab = get_lab_assignment(lab_no, term)
lab_spoof = get_lab_assignment(lab_no_spoof, term)
print(lab)
print(section)

# for student in get_students(section):
#     print(student.user['name'])

update_grades(lab_spoof, section, student_grades)

print()