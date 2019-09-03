#Written By Rob Becker, May 30, 2019
#program for car rental by type"rate", w/ or w/o insurance, for 1 to many days
print("\n")
print("Robert's Car Rental\n")
print("Select Vehicle Model")
#Choice allows users to select vehicle type, rates are cost per type per day
choice = input("Compact Car(C) or Intermediate(I) or Standard(S): ")
if choice == "C":
    rate = (30)
elif choice == "I":
    rate = (40)
elif choice == "S":
    rate = (50)
#Choice of insurance or no insurance followed by cost per day in dollars
choice = input("Insurance Yes(Y) or No(N): ")
if choice == "Y":
    insurance = 15
elif choice == "N":
    insurance = 0
#Duration allows a user to input their rental duration in days
duration = float(input("For what duration would you like to rent the vehicle?(Days): "))
#Calculates vehicle type plus insurance costs per day
DailyCost = rate + insurance
#Calculates total cost per day multiplied by the duration intinger to achieve total cost of purchase
TotalCost = DailyCost * duration
#Output statement showing the total cost of purchase for entire duration
print("\nThe cost of your rental is $" + str(TotalCost))
