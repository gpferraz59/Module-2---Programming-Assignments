# Name : Gislaine Paula Ferraz
# File Name : M02 Case-Study.py
# Description : The purpose of this assignment is to apply my knowledge 
#               and skill in coding if...else and while statements in Python. 

while True:
    last_name = input("Enter student's last name or (enter 'ZZZ' to end program):\n")
    last_name = last_name.capitalize()

    if last_name.upper() == "ZZZ":
        print("\n---Ending Program---")
        break

    first_name = input("Enter student's first name:\n")
    first_name = first_name.capitalize()
    student_gpa = float(input("Enter student's GPA:\n"))

    if student_gpa >= 3.5:
        print("\nThe student ", first_name, last_name, "has made the Dean's List\n")
    elif student_gpa >= 3.25:
        print("\nThe student", first_name, last_name, "has made the Honor Roll\n")
    
    