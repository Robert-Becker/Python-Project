#Original code written by Robert Becker on June 10, 2019
#Last Modified: June 10, 2019 by Robert Becker
#Last Modification Notes: Code was created to estimate the minimum cost of property insurance needed at 80% of the cost to rebuild the structure.
#Defines cost variable, prompts for user input of property value
cost = float(input("Enter the value of the property you wish to insure: "))
#Defines function insurance with input from cost variable
def insurance(cost):
#returns 80% of the user input value
    return cost * .80
#Calls user-defined function insurance using the cost variable
insurance(cost)
#Prints output message with functions output
#format variable used to round value to 2 decimal places
print("You should minimally insure your property for $" + str("{:.2f}".format(insurance(cost))) + " dollars.")
