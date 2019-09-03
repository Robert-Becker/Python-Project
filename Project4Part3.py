#Written by Robert Becker on June 12, 2019
#Last Modified: June 12, 2019
#Last Modification Notes: Program was written to calculate future value of on investment using the formula F=P(1+i)^t
#Prompt explaining the purpose of this program.
print("Use this calculator to display the future value of an investment.")
#User prompt indicating the items necessary to use the calculator(present value, monthly interest rate, and the number of months the investment will sit in the account
print("You will need to know the current sum of your investment, the monthly interest rate, and the number of months you wish to let your investment grow.")
#Creates variable for the principle loan amount and asks the user to enter their current investment total
principle = float(input("Please enter the amount you wish to invest: $"))
#Creates variable for the monthly interest rate and asks the user to enter the monthly interest rate they will be using
interestRate = float(input("Please enter the monthly interest rate: "))
#Creates variable for the amount of time the investment will grow in terms of months
timeMonths = float(input("Please enter the number of months that the investment will grow: "))
#User defined function defines the formula F=P(1+i)^t
def investmentCalculator(principle, interestRate, timeMonths):
    return principle*(1+(interestRate/100))**timeMonths
#Calls the user defined function with the variables principle, interestRate, & timeMonths
investmentCalculator(principle, interestRate, timeMonths)
#Output from the program presented to the user
print("The future total of the investment will be $" + str("{:.2f}".format(investmentCalculator(principle, interestRate, timeMonths))))