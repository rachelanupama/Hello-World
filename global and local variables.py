#global and local variables

# variables inside and outside the function are called global and local variables.
#a variable defined above the func and is accessible to the entire global space is called global variable.

#first case of global variable

'''a = 3
def check():
    print("inside value is",a)
check()
print("outside value is",a)'''

#second case of global variable

'''a = 4
def check1():
    a = 5
    a = a**2
    print("inside value is",a)
check1()
print("outside value is",a)'''

#thrid case of both global and local variables
'''a = 2
b = 9
def check2():
    a = 10
    print("inside value is ",a)
    a = 5
    print("updated value is ", a+10)
    b = 13 #local variable
    b = b+a
    print("value of b is",b)
check2()
print("a value is ",a)
print("b value is",b)'''

#usuage of global keyword

'''a= 4
def final():
    global a,b
    print("inside value is ",a)
    a = 3
    print("updated value is",a)
    #global b
    b = 20
    b = b+a
    print("value of b is",b)
final()
print("a value is ",a)
print("b value is",b)'''

'''usage of global variable -----> when user wants to access the global variable inside the function directly
and carry forward the updated value even outside the func then we need to use global keyword'''

#generators
#no tuple comprehension in above cases if we remove those braces and keep parenthesis then the outcome is generator

'''a = [i for i in range(16)]
print(a)
print(type(a))'''

'''a = (i for i in range(16))
print(a)
print(type(a))'''

'''a = [i for i in range(16)]
print(*a) #unpack it
print(type(a))'''

'''a = [i for i in range(16)]
#print(list(a))
#print(tuple(a))
print(set(a))
print(type(a))'''

#generators ->  it is also a function which can be used as an iterator (loop) by producing group of values, where we used "yield" keyword
#yield vs return
#return will terminate the func, where as yield can pass the func and go on with every successive iteration

'''a,b = [int(x) for x in input("enter the values"). split(",")]
def check(a,b):
    while a < b:
        yield a
        a = a+1
        yield a
print(*check(a,b))'''

'''a,b = [int(x) for x in input("enter the values"). split(",")]
def check(a,b):
    while a < b:
        a = a+1
        return a
print(check(a,b))'''

#yield vs return

'''def  mygen():
    return "python"
    return "java"
    return "c"
    return "python", "java","c"
print(*mygen())'''

def mygen():
    yield "apple"
    yield "grapes"
    yield "orange"
#print(*mygen())

#next()
d = mygen()
print(next(d))
print(next(d))
print(next(d))



















































































 





































































