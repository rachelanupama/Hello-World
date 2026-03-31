#anonymous functions are nameless functions and we use a keyword called as lambda to create anonymous function

#write a function to calculate 2*x+5 where x = 5
'''def f(x):
    print(2*x+5)
f(5)'''


'''def f():
    x = int(input("enter the x value"))
    print(2*x+5)
f()'''

#syntax
#a = lambda arg:expression

'''a = lambda x:2*x+5
print(a(5))'''

'''a = int(input("enter a value"))
b = lambda x:2*x+5
print(b(a))'''

'''a = lambda x,y:x*y
print(a(2,3))'''

'''a = int(input("enter a value"))
b = int(input("enter b value"))
c = lambda x,y:x*y
print(c(a,b))'''

'''a = 'codegnan'
b = lambda a:a.upper()
print(b(a))'''

'''a = input("enter data:")
b = lambda a:a.upper()
print(b(a))'''

'''a = 'python course'
b = lambda a:a.title()
print(b(a))'''

'''a = input("enter data:")
b = lambda a:a.title()
print(b(a))'''


'''a = input("enter first name: ")
b = input("enter last name: ")
c = lambda a,b: ((a+" "+b).title())
print(c(a,b))'''

'''a,b = [x for x in input("enter the fname and lname"). split(" ")]
c = lambda a,b: ((a+" "+b).title())
print(c(a,b))'''

#filter()
#b =[]
#a = [10,30,40,55,67,89,90,95,97,100]
'''for i in a:
    if i % 2 == 0:
       b.append(i)
print(list(b))'''

# [],(),{}
'''a = []
print(type(a))

b = ()
print(type(b))

c = {}
print(type(c))

d = set()
print(type(d))'''

#filter keyword

'''a = [ [], (),{},set(), "" , None, 3,5.6,"python",5+8j,True,False]
b = list(filter(None,a))
print(b)'''

#map() each obj from a collection and forms a new collection

'''a = [10,22,33,44,55]
b = [1,33,1,55,22]
c = list(map(max,a,b))
print(c)
d = list(map(min,a,b))
print(d)'''

'''a = input("data1: ")
b = input("data2: ")
print(a+b)'''

'''a,b = [x for x in input("enter the names: ").split(",")]
print(a+b)'''

'''a,b = input("enter the names).split(",")
print(a+b)'''

'''a = int(input("a value"))
b = int(input("b value"))
print(a+b)'''

'''a,b = [int(x) for x in input("enter the values"),split(",")]
print(a+b)'''

''''a,b = int(input("enter the values").split(","))
print(a+b)''' #ERROR


'''a= list(map(int,input("enter the values").split(",")))
print(a)
print(type(a))'''

'''a= tuple(map(int,input("enter the values").split(",")))
print(a)
print(type(a))'''

'''a= set(map(int,input("enter the values").split(",")))
print(a)
print(type(a))'''

            






























        





















































































































