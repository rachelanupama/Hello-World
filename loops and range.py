#while loop

'''a = 3
b = 7
while a < b:
    print(a)'''

'''a = 5
while a>1:
    print(a)
    a=a-1'''

'''a = 5
while a>1:
    a=a-1
    print(a)'''

'''a = 5
while a>1:
    print(a)
    a = a+1'''

'''a = 1
while a < 10:
    print(a)
    a+=1'''

'''while True:
    age = int(input("enter the age"))
    if age >= 18:
              print("eligible to vote")
    else:
        print("not eligible to vote")'''

'''while True:
            n = input("enter a value").lower()
            vow = ['a', 'e','i','o','u']
            if n in vow:
                print ("it is a vowel")
            else:
                print("consonant")'''


#range()
#the range function returns a sequence of numbers starting from 0 by default and increments by one by one and stops before a specified number

'''for i in range(5):
    print(i)'''

'''for i in range (10,20):
    print(i,end = " ")'''

#(start,stop,step)

'''for i in range(0,20,2):
    print(i,end = ',')'''

'''for i in range(5,50,5):
    print(i,end = ',')'''

'''for i in range(3,30,3):
    print(i,end = ',')'''

#grades task

'''while True:
    i = int(input("Enter grade"))
    if i in range(91,101):
        print("Grade A")
    elif i in range(81,91):
        print("Grade B")
    elif i in range(71,81):
        print("Grade C")
    elif i in range(50,71):
        print("Grade D")
    else:
        print('Fail')'''

#diff  between break,continue and pass
#the break stmt is used to terminate the entire loop
#the continue stmt is used to skip the current iteration and continue the rest of the code
#pass stmt is a null stmt, it does nothing but syntactically we need it

#break
'''a = 10
while a > 1:
    print(a)
    a = a-1
    if a == 5:
        break'''

'''a = 10
while a>1:
    a =a-1
    if a == 5:
        break
    print(a)'''

'''a = 10
while a>= 1:
    print(a)
    a = a-1
    if a == 5:
        break'''

'''for i in range(25):
    if i == 15:
        break
    print(i)'''

'''a = "python"
for i in a:
    if i == "h":
        break
    print(i)'''

#continue

'''a = 10
while a > 1:
    print(a)
    a = a-1
    if a==10:
        continue'''

'''a = 20
while a > 1:
    a = a-1
    if a == 10:
        continue
    print(i)'''

'''a = 10
for i in range(10):
    if i ==6:
        continue
    print(i)'''

'''a = "rachel"
for i in a:
    if i == "e":
        continue
    print(i)'''


#pass

'''a = 20
while a>2:
    print(a)
    a=a-1
    if a == 10:
        pass'''

'''for i in range(10):
    if i == 5:
        pass
    print(i)'''

a = "python"
for i in a:
    if i=='t':
        pass
    print(i)

































































