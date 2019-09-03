#Written By Robert Becker June 7, 2019
#Program to calculate ideal weight for a patient
#Initial Screen Output/Greeting
print("Find Your Patients Ideal Weight" + "\n")
print("Input Patient's Height")
#height variable / user input
height = float(input("Please Enter Patient's Height (In Inches): "))
#Prompt
print("Please Select Gender")
#Variable Condition - Male or Female
choice = input("Male(M) or Female(F): " + "\n")
#Choice Calculation for Females
if choice == "F":
    heightVariable = height * 3.5
    heightVariable = heightVariable - 108
#Choice Calculation for Males
elif choice == "M":
    heightVariable = height * 4
    heightVariable = heightVariable - 128
#Output From Script
print("The Ideal Weight For Your Patient: " + str("{:,.2f}".format(heightVariable) + " Pounds."))