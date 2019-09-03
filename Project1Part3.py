print("")
print("")
print("Select Service")
print("")
choice = input("Makeover(M) or HairStyling(H) or Manicure(N) or Permanent Makeup(P): ")
if choice == "M":
    cost = 125
elif choice == "H":
    cost = 60
elif choice == "N":
    cost = 35
elif choice == "P":
    cost = 200
print("")
print("Select Discount")
print("")
choice = input("10% Discount(10) or 20% Discount(20) or No Discount(0): ")
if choice == "10":
    discount = 0.9
elif choice == "20":
    discount = 0.8
elif choice == "0":
    discount = 1.0
print("")
TotalCost = (cost * discount)
print("Total: $" + str((TotalCost)))
