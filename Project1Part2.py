print("")
print("")
print("Employee Salary Calculator")
print("")
hr = float(input("Hours Worked: "))
choice = input("Tester(1) or Developer(2) or Manager(3): ")
if choice == "1":
    rate = (35)
    salary = rate * hr
elif choice == "2":
    rate = (50)
    salary = rate * hr
elif choice == "3":
    rate = (65)
    salary = rate * hr
print("")
print("Employee Salary This Period $" + str("{:,.2f}".format(salary)))
