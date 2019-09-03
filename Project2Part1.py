#Written by Rob Becker, May 30, 2019
#Greeting
print("\nPlease input hours parked below\n")
#Parking Attendant would manually enter the length of parking in hours
x = input("Length of Stay(Hours): ")
x = float(x)
#Statements following determine cost in dollars based on input from parking Attendent
if 0 < x <= 3:
    cost = 5
elif 3 < x <= 4:
    cost = 6.5
elif 4 < x <= 5:
    cost = 8
elif 5 < x <= 6:
    cost = 9.5
elif 6 < x <= 7:
    cost = 11
elif 7 < x <= 8:
    cost = 12.5
elif 8 < x <= 9:
    cost = 14
elif 9 < x <= 10:
    cost = 15.5
elif 10 < x <= 11:
    cost = 17
elif 11 < x <=24:
    cost = 18
#Output of program to user display
print("\nCustomer Total: $" + str(cost))
