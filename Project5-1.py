#Original Code Written by Robert Becker
#Date Written  - 6/25/2019
#Program was written to calculate end of semester scores for students by using an input file with a single space used as the delimiter between items

inputFile = open("scores.txt", "rt")  #Define Input FIle Variable, opens file to read text
fileData = inputFile.readlines()  #defines fileData variable, tells it to look at each line of the file
inputFile.close()#closes file we opened

for line in fileData:#specifies what to do for each line of data from fileData
    items = line.split()#tells the file to create logical indexes with each space character in the file
    name = str(items[0]) + " " + str(items[1])#creates name variable set to items 0 and 1 / First / Last Names
    assignmentScores = int(items[2]) + int(items[3]) + int(items[4]) + int(items[5]) + int(items[6])#creates assignmentScores variable and adds all the assignments together
    quizScores = int(items[7]) + int(items[8]) + int(items[9]) + int(items[10]) + int(items[11])#creates quizScores variable and adds all the quizzes together
    examScores = int(items[12]) + int(items[13])#creates examScores variable and adds all the exams together
    computeAverage = (assignmentScores/500*.4 + quizScores/100*.2 + examScores/200*.4)*100#creates computeAverage variable that find the students weighted final score

    if 90 <= computeAverage <= 100: #Creates conditional statements that changes the total grade from a number to a letter
        grade = "A"
    if 80 <= computeAverage <90:
        grade = "B"
    if 70 <= computeAverage <80:
        grade = "C"
    if 60 <= computeAverage <70:
        grade = "D"
    if 0<= computeAverage <60:
        grade = "F"

    print(name + " " + str(grade))#Prints name variable, adds a space, and prints final letter grade

