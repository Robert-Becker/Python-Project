#Written by Robert Becker on June 12, 2019
#Last Modified: June 12, 2019
#Last Modification Notes: Program was written to calculate the annual cost of ownership of an automobile
#Prompt to inform user of the data they will need to enter
print("Please enter the estimated monthly cost of the following expenses below. Loan Payment, Insurance, Gas, and Maintenance.")
#Prompt for user to input their Loan Payment Information
payment = float(input("Please enter the monthly loan payment cost: "))
#Prompt for user to input their Insurance Cost Information
insurance = float(input("Please enter the monthly insurance cost: "))
#Prompt for user to input their Monthly Gas Cost
gas = float(input("Please enter the cost of gas usage per month: "))
#Prompt for user to input their Estimated Maintenance Cost per month
maintenance = float(input("Please enter the estimated cost of Maintenance per month: "))
#User Defined Function to calculate annual cost from monthly cost totals.
def yearlyCostCalculator(payment, insurance, gas, maintenance):
    return (payment + insurance + gas + maintenance) * 12
#Calls the user defined function for yearlyCostCalculator
yearlyCostCalculator(payment, insurance, gas, maintenance)
#Generates the output of the calculation to the user with written statement
print("\nThe estimated yearly expenses total: $" + str("{:.2f}".format(yearlyCostCalculator(payment, insurance, gas, maintenance))))
