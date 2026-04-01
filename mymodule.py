#module,library,package

#a module in python is a single python file, it consists python code
# it typically consists of functions,classes and variables that can be used in other python scripts or programs
# examples of modules are math.py, random.py, mymodule.py

#package
#a package in python is a directory containing one or more python modules and an __init__.py file
#the __init__.py file can be empty or contain intilization code for the package
#examples of packages include numpy, pandas, django

#library
#libraries consists of multiple modules and packages, organized to serve a particular purpose or domain
#examples of libraries such as requess, numpy, pandas and matplotlib

#note: every python file is a module and import is a keyword and every python file is saved internally with variable name as __main__

'''def greetings(name):
    print("welcome", name)'''

'''a = 4
b = 8
print(a+b)'''

'''a = int(input("a value"))
b = int(input('b value'))
print(a+b)'''

#details = {"idnos" : [10,20,30], "names": ["apple", "orange"], "cities": ["vij","gun"]}

if __name__ == "__main__":
    a = [10,20,30]
    a.append("code")
    a.extend("code")
    print(a) #no mudule because its script

def dummy():
    if __name__ == "__main__":
        print("this program is run as script")
    else:
        print("this program is run as module")
dummy()
    
























