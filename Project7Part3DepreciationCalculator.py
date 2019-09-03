"""
Original Code Written By Robert Becker
Created on July 21, 2019
Last Modified on July 21, 2019
Program was designed to calculate item depreciation using straight-line or double-declining balance methods.
Project7 Part3
"""

description = input("Enter the name of the item purchased: ")
year = int(input("Enter year purchased: "))
cost = int(input("Enter cost of item: "))
cost_constant = cost
lifetime = int(input("Enter estimated life of item (in years)) : "))
lifetime_constant = lifetime
method = input("Enter the method of depreciation (SL or DDB): ")

if method == "SL":
    print("Description:"
          " " + description)
    print("Year of purchase: " + str(year))
    print("Cost: $" + str(round(cost, 2)))
    print("Estimated Life: " + str(lifetime) + " years")
    print("Method of depreciation: Straight-Line \n")
    print("           Value At    Amount Deprec   Total Depreciation")
    print("          Beg of Yr.     During Year      To End of Year")
    sl_amt_dep = (cost * (1 / lifetime))
    total_dep = sl_amt_dep
    while lifetime == lifetime:
        ddb_amt_dep = (cost_constant * (1 / lifetime_constant))
        total_dep = ddb_amt_dep
        print(str(year) + "       " + str(cost_constant) + "          " + str(ddb_amt_dep) + "        " + str(total_dep))
        lifetime -= 1
        year += 1
        break
    while lifetime > 0:
        cost = cost - (cost_constant * (1 / lifetime_constant))
        ddb_amt_dep = (cost_constant * (1 / lifetime_constant))
        total_dep = ddb_amt_dep + total_dep
        print(str(year) + "       " + str(cost) + "        " + str(ddb_amt_dep) + "        " + str(total_dep))
        lifetime -= 1
        year += 1
        continue
    while lifetime == 0:
        continue
elif method == "DDB":
    print("Description: " + description)
    print("Year of purchase: " + str(year))
    print("Cost: $" + str(round(cost, 2)))
    print("Estimated Life: " + str(lifetime) + " years")
    print("Method of depreciation: Double-Declining-Balance \n")
    print("           Value At    Amount Deprec   Total Depreciation")
    print("          Beg of Yr.     During Year      To End of Year")
    ddb_amt_dep = (cost * (2 / lifetime))
    total_dep = ddb_amt_dep
    while lifetime == lifetime:
        print(str(year) + "       " + str(cost) + "         " + str(ddb_amt_dep) + "         " + str(total_dep))
        lifetime -= 1
        year += 1
        break
    while lifetime > 1:
        if cost != 0:
            cost = cost - (cost * (2/lifetime_constant))
            ddb_amt_dep = (cost * (2/lifetime_constant))
            total_dep = ddb_amt_dep + total_dep
            print(str(year) + "       " + str(cost) + "        " + str(ddb_amt_dep) + "        " + str(total_dep))
            lifetime -= 1
            year += 1
        continue
    while lifetime == 1:
        cost = cost - (cost * (2 / lifetime_constant))
        print(str(year) + "       " + str(cost) + "         " + str(cost) + "      " + str(cost_constant))
        lifetime -= 1
        year += 1
else:
    print("\n")






