''''account = 100000
card = "c"
pwd = 1234'''
'''print("ATM Application")
print(("Insert the card----------->"))
id = input()
if id == "c":
    print("Welcome")
else:
    print("Invalid Username")
print("Enter the pin: ")
pd = int(input())
if pd == 1234:
    print("Options: 1. Balance Enquiry.  2. Withdraw")
    op = int(input())
    if op == 1:
        print("Balance is",account)
    elif op == 2:
        print("Enter the amount: ")
        a = int(input())
        print("Remaining balance is ",account - a)
    else:
        print("Option is not available")
else:
    print("Invalid pin")'''
while True:
    account = 100000
    card = input("insert the card")
    pwd = 1234
    if card == "c":
        print("Welcome Rachel . . . . . . ")
        password =int(input("Enter the password"))
        if passoword == pwd:
            option = int(input('''choose the option
                                                     1. balance enq
                                                     2. withdraw '''))
            if option == 1:
                print("your account balance is", account)
            elif option == 2:
                money = int(input("enter the money"))
                print(money)
                balance = account - money
                print("remaining balance is", balance)
            else:
                print("Exit. . . . .")
                break
        else:
            print("Incorrect password")
    else:
        print("Incorrect username")





































