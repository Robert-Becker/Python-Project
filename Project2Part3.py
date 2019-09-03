#Written By Rob Becker, May 30,2019
#Program Prints % and Letter Grade for Students
#Requires user input

#Greeting
print("\nStudent Grade Calculator\n")
#Variables
StudentName = input("Please enter student's name: ")
q = float(input("Please enter total quiz score: "))
a = float(input("Please enter total assignment score: "))
m = float(input("Please enter midterm exam score: "))
f = float(input("Please enter final exam score: "))
#Function Calculates grade percentage rounded to 2 digits
averageScore = round((q * .15) + (a * .40) + (m * .20) + (f * .25), 2)
#Makes Letter Grade based on averageScore percentage
if 97 < averageScore <= 100:
    grade = "A+"
elif 94 < averageScore <= 97:
    grade = "A"
elif 90 < averageScore <= 94:
    grade = "A-"
elif 87 < averageScore <= 90:
    grade = "B+"
elif 84 < averageScore <= 87:
    grade = "B"
elif 80 < averageScore <= 84:
    grade = "B-"
elif 77 < averageScore <= 80:
    grade = "C+"
elif 74 < averageScore <= 77:
    grade = "C"
elif 70 < averageScore <= 74:
    grade = "C-"
elif 0 <= averageScore <= 70:
    grade = "F"
#output shows student names, numerical score, and letter grade
print("\n" + StudentName + ", received an average score of " + str(averageScore) + "%, " + str(grade) + ".")

