print(" ")
print("Estimate Your Monthly Payment")
print(" ")
P = float(input("Price of Vehicle: "))
D = float(input("Initial Down Payment: "))
R = float(input("Annual Percentage Rate: "))
N = float(input("Length of Contract(Years): "))
i = R/1200
n = N*12
M = ((P - D)*i*pow((1+i), n)/(pow((1+i), n) - 1))
X = round(M,2)
print(" ")
print("Your Estimated Monthly Payment:  $" + str(X) )