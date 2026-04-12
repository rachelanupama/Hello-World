#OOPs
# a class contains attributes or variables and methods or functions that can manipulate the data
# a class is the blueprint of an object
# an object is an intiation of a class
# methods or functions define inside the body of thr class

#four pillars of oops
# polymorphism - operator overloading, operator overriding, method overloading, method overriding
# inheritance - single, multiple, multi level
# encapsulation - public data, _protected data, __private data
# abstraction - abstract class, abstract method

#syntax
'''class classname():
    #attributes
    name = "python"
    year = 2026
    place = "vij"
    def fname(self):
        print(statements. . . . . .)
a = classname()
a.fname()'''

#class declaration
'''class Details():
    name = "rachel"
    sub = "python"
    city = "vij"
    def display(self):
        print(self.name,self.sub,self.city)
a = Details()
print(dir(a))
a.display()'''

#object instantiation
'''class Details():
    def Data (self,name,sub,place):
        self.name = name
        self.sub = sub
        self.place = place
    def display(self):
        print(self.name,self.sub,self.place)
a = Details()
a.Data("rachel","python","guntur")
b = Details()
b.Data("abc","java","vij")
a.display()
b.display()'''


class Details():
    def Data (self):
        self.name = input("Enter a name")
        self.sub = input("Enter a subject")
        self.place = input("Enter a place:")
    def display(self):
        print(self.name,self.sub,self.place)
a = Details()
a.Data()
a.display()




























































