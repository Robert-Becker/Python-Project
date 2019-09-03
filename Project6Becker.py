"""Original Code Written By Robert Becker
Written On July 10, 2019
Last Modified by Robert Becker
Last Modified on July 16, 2019
Program simulates a banking ATM
#Not sure how to update bank account if user does multiple operations
#Not sure how to export file properly or not sure how to cleanse messy input file
#Not sure how to fix error from failing to enter correct acct/pin combo
#Not sure how to update dictionary with tuple as key pair
#Don't understand classes, functions, variables in depth.
#Started to fall apart when working with multiple functions.
#Could not figure out how to do any of this with lists.
"""
d = {}
accounts = open("accounts.txt", "r+")
for line in accounts.readlines():
    (key1, key2, value) = line.split(';')
    d[(key1, key2)] = value
    #exDict = {'d': d}


def login():
    global balance
    global acct_num_input
    global acct_pin_input
    print("Welcome to your bank. \nPlease use the touchpad below to get started.")
    acct_num_input = input("Please enter your account number: ")
    acct_pin_input = input("Please enter your account pin: ")
    balance = d[acct_num_input, acct_pin_input]
    print("Your Balance is " + str(balance))
    menu()


def menu():
    global new_balance
    selection = input("Would you like to Fast-Withdraw(F), Withdraw(W), Deposit(D), or Quit(Q): \n")
    if selection == "F" or selection == "f":
        print("Withdraw $20,  Press (1)\nWithdraw $40,  Press (2)\nWithdraw $60,  Press (3)\nWithdraw $100, Press (4)")
        fast_withdraw = int(input("Enter your selection now: "))
        if fast_withdraw is 1:
            if float(balance) >= 20:
                new_balance = float(balance) - 20
                print("Your new balance is $" + str(new_balance))
                menu()
                #Code for later iterations
                #print(d.items())
                #with open("newaccounts.txt", "w+") as newaccounts:
                    #print(d.copy(), file=newaccounts)
            else:
                print("Cannot withdraw more than your account balance")
                menu()
        elif fast_withdraw is 2:
            if float(balance) >= 40:
                new_balance = float(balance) - 40
                print("Your new balance is $" + str(new_balance))
                menu()
            else:
                print("Cannot withdraw more than your account balance")
                menu()
        elif fast_withdraw is 3:
            if float(balance) >= 60:
                new_balance = float(balance) - 60
                print("Your new account balance is $" + str(new_balance))
                menu()
            else:
                print("Cannot withdraw more than your account balance")
                menu()
        elif fast_withdraw is 4:
            if float(balance) >= 100:
                new_balance = float(balance) - 100
                print("Your new account balance is $" + str(new_balance))
                menu()
            else:
                print("Cannot withdraw more than your account balance")
                menu()
        else:
            print("Input Error, Please try again.")
            print("Current Account Balance: " + str(balance))
            menu()
    elif selection == "W" or selection == "w":
        print("You selected withdraw.")
        custom_withdraw = float(input("Please enter the amount you'd like to withdraw: "))
        if custom_withdraw <= float(balance):
            new_balance = float(balance) - float(custom_withdraw)
            print("Your new account balance is: " + str(new_balance))
            menu()
        else:
            print("You cannot withdraw more than $" + balance)
            menu()
    elif selection == "D" or selection == "d":
        deposit = float(input("Please enter the amount of the deposit: $"))
        new_balance = float(balance) + float(deposit)
        print("Your new account balance is $" + str(new_balance))
        menu()
    elif selection == "Q" or selection == "q":
        print("Thank you for your patronage")
        print(d.items())
        input("Press Enter to begin: ")
        menu()
    else:
        print("You've enter an incorrect value. Please try again.")
        menu()


login()
