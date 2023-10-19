from read_excel import read_excel
from write_to_canvas import *

print("CPSC 121 Lab Grade Automation Script by Aprameya Aithal\n")

section_name = input("Enter section name (eg: L12): ")
lab_no = int(input("Enter lab number (eg: Enter 2 for Lab 02): "))
lab_no_spoof = None
if lab_no_spoof is not None:
    lab_no = lab_no_spoof
term = "2023W1"
cpsc_121 = 123413

student_grades = read_excel(f'{section_name}.xlsx', lab_no=lab_no)
welcome_user()
load_course(cpsc_121)
section = get_lab_section(section_name, term)
lab = get_lab_assignment(lab_no, term)
print(lab)
print(section)

# for student in get_students(section):
#     print(student.user['name'])
if input("Confirm? (Y/n)") in ["Yes", "Y", "Ya", "Of course"]:
    update_grades(lab, section, student_grades)
else:
    print("Cancelled")

