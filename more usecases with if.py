#electricity bill calculator

'''units = int(input('enter units used'))
if units <= 100:
    print (units*5)
elif units <= 200:
    print (units*7)
else:
    print (units*10)'''

#BMI
'''wt = float(input("enter the weight"))
ht = float(input("enter the height"))
bmi = wt/(ht*ht)
if bmi < 18.5:
    print('Underweight')
elif bmi < 24.9:
    print("Normal")
elif bmi < 29.9:
    print("Overweight")
else:
    print("Obese")'''

#Simple Calculator

'''num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
op = input("enter the operation")
if op == '+':
    print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1*num2)
elif op == '/':
    print(num1/num2)
else:
    print('invalid operator')'''

#Triangle Type

'''len1 = int(input("enter the length of the first side"))
len2 = int(input("enter the length of the second side"))
len3 = int(input("enter the length of the third side"))
if len1 == len2 and len2 == len3:
    print('Equilateral')
elif len1 == len2 or len2 == len3 or len1 ==len3:
    print('Isosceles')
else:
    print("Scalene")'''


#salary tax calculation

'''salary = int(input("Enter your salary: "))
if salary < 300000:
    tax = 0
elif salary <= 700000:
    tax = salary * 0.10
elif salary <= 1000000:
    tax = salary * 0.20
else:
    tax = salary * 0.30
print("Tax amount:", tax)'''

#character type detector

'''char = input("Enter a character")
if char.islower():
    print("Lowercase")
elif char.isupper():
    print('Uppercase')
elif char.isdigit():
    print("Digit")
else:
    print("special character")'''

#Online Shopping Delivery

'''amt = int(input("enter the amount"))
location = input("enter the type of delivery: local, national or international").lower()
if amt < 2000:
    print("free delivery!.......Total Bill :" + amt)
elif location == 'local':
    print("delivery cost = 50........Total Bill :",amt+50)
elif location == 'national':
    print("delivery cost = 100........Total Bill :" ,amt+100)
elif location == 'international':
    print("delivery cost = 300........Total Bill :",amt+300)
else:
    print("Invalid")'''

'''amt = int(input("enter the amount"))
location = input("enter the type of delivery: local, national or international").lower()
if amt > 2000:
    delivery = 0
elif location == 'local':
    delivery = 50
elif location == 'national':
   delivery = 100
elif location == 'international':
    delivery = 300
else :
    print("Invalid")
    delivery = 0
print('Delivery Cost : ',delivery)
print('Total : ',amt + delivery)'''

#ATM Withdrawal

'''account_balance =int( input("Enter the balance"))
withdrawl_amount =int( input("Enter the withdrawl amount "))
if withdrawl_amount >  account_balance:
    print('Insufficient balance')
elif withdrawl_amount % 100 == 0:
    print("Transaction Suscessful")
else:
    print("Enter amount in multiples of 100")'''

#Voting Eligibility

'''age = int(input("Enter the age:"))
c = input("Are you a citizen? (Y/N)").lower()
if age < 18:
    print("Too young to vote")
else :
    if c == 'y':
        print("Eligible to vote")
    else:
        print("Must be a citizen to vote")'''

#Scholarship System

'''marks = int(input("Enter the marks"))
income = int(input('Enter the income'))
if marks >= 90:
    if income < 300000:
        print("Full scholarship")
    else:
        print("Half scholarship")
elif marks < 90 and marks > 74:
    print("Partial Scholarship")
else:
    print("No Scholarship")'''




