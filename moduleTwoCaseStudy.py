#Cristian Alvarez
#Module Two Case Study
#App will take students first and last name and their gpa to check and see if the student will make the Deans List

lastName = ""
firstName = ""
gpa = 0.0

while True:
    lastName = input("Enter your last name: ")
    if lastName == "ZZZ":
        break
    firstName = input("Enter your first name: ")
    gpa = float(input("Enter your GPA: "))
    if gpa >= 3.5:
        print("You have made the deans list!")
    elif gpa >= 3.25:
        print("You made honor roll!")
    else:
        print("Try next time!")