#variable length arg automatically store in tuple and we use star arg

'''def check():
    print(a)
    print(type(a))
check()
check(2,3,4,5,6)
d = [1,2,3,4,5]
check(*d)
e = {10,20,30,40}
check(*e)
f = {"name" : "rachel", "course" : "python"}
check(*f)'''

'''def check1(*a):
    d = "1"
    print(a)
    print(type(a))
    for i in a:
        d += str(i)
        print(d)
check1()
check1(2,3,4,5)
check1(1,2,3,4.5,6.9)
check1(1,2,3,4.6,"rachel")'''


"""def check1(*a):
    d = "1"
    print(a)
    print(type(a))
    for i in a:
        if type(a) in (int,float):
            d += i
            print(d)
check1(1,2,3,4.6,"rachel")"""

# ** args (kwargs)

'''def check2(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i, a[i])
    for i in a.items():
        print(i)
check2()
details={"idnos":[10,20,30],
         "names":['priya', 'sita', 'raj'],
         "status":["P", "A", "P"]}
check2(**details)'''


#both * and ** usuage
'''def final(*a, **b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i, j in b.items():
        print("key is", i)
        print("value is", j)
final()
data=(2, 3, 4, 5, 4.3, 2.3)
final(*data)
details = {"idnos":[10,20,30],
         "names":['priya', 'sita', 'raj'],
         "status":["P", "A", "P"]}
final (**details)
final(*data,**details)'''

#ascii
#chr()
'''print(chr(76))
print(chr(65))
print(chr(90))
chr("a") #error

#ord
print(ord("a"))
print(ord("Z"))
print(ord(2)) #error'''

'''for i in range(65,91):
    print(chr(i), end = " ")

for i in range(97,123):
    print(chr(i), end = " ")'''


n = input()
for i in n:
    print(i ,"-" ,ord(i))





















































































































