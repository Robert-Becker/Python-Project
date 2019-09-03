#Written by Robert Becker on June 7th, 2019
#Program Calculates Training Heart Rate
#Prompt to enter users age
ageVariable = float(input("Please Input Your Age: "))
#Calculation to predict maximum heartrate based on age
maxHeartRate = 220 - ageVariable
#Prompt for resting heartrate
restingHeartRate = float(input("Please Enter Your Resting Heart Rate: "))
#Calculation Max HR minus Rest HR
calculationHeartRate = maxHeartRate - restingHeartRate
#Calculation multiply calculationHeartRate by 60%
calculationHeartRate = calculationHeartRate * 0.6
#Calculation add restingHeartRate to previous calculation
THR = calculationHeartRate + restingHeartRate
#Displays the calculated THR to the user (Rounded to whole#)
print("Your Estimated Training Heart Rate(THR) is " + str(round(THR)) + " BPM")
