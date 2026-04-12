#polymorphism
#opreation overloading
'''a=3;b=5
print(a+b)
print(a._add_(b))
print(a._add_(6))
print(a._sub_(2))
print(a._mul_(b))
#print(a._div_(2))
print(a._pow_(2))
print(a._ge_(2))
print(a._le_(4))
a=[1,2,3,4,5];b=[6,7,8,9,10]
print(a._add_(b))
print(a._getitem_(2))
print(a._getitem_(4))
a="code";b="gnan"
print(a._add_(b))
a="python";b="course"
print(a._add_(" "+b))
print("pavithra"._add_(" "+"k").title())'''

#operator over riding
'''class A():
    def _init_(self,a):
        self.a=a
    def _add_(self,value):
        return self.a*value.b
class B():
    def _init_(self,b):
        self.b=b
x=A(4)
y=B(5)
#x=4
#y=5
print(x+y)->9
print(x+y)'''


#method overloading
class New():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is ",a+b+c)
        elif a!=None and b!=None:
            print("the produt is",a*b)
        else:
            print("program ends")


a=New()
a.sum(2,3,4)
a.sum()
a.sum(5,6)

#method overriding
class Animal():
    def speak(self):
        print("animal can make sounds")
class Dog():
    def speak(self):
        print("dog barks")
a=Animal()
b=Dog()
a.speak()
b.speak()
