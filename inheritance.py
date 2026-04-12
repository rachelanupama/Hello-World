#single inheritance

'''class RBI(): #parent class
    cash = 100000
    def available_cash(self):
        print("available cash is",self.cash)
        print("available cash is", RBI.cash)
class SBI (RBI): #child 1
    pass
class HDFC(RBI): #child 2
    cash = 50000
    def new_cash(self):
        print("new cash is",self.cash+self.cash)
        print("new cash is",self.cash+RBI.cash)
b = HDFC()
b.available_cash()
b.new_cash()'''

'''class RBI(): #parent class
    cash = 100000
    def available_cash(self):
        print("available cash is",self.cash)
        print("available cash is", RBI.cash)
class SBI (RBI): #child 1
    cash = 25000
    def sbicash(self):
        print("new cash is", self.cash+self.cash)
        print("new cash is",self.cash+RBI.cash)
class HDFC(RBI): #child 2
    cash = 50000
    def new_cash(self):
        print("new cash is",self.cash+self.cash)
        print("new cash is",self.cash+RBI.cash)
b = HDFC()
b.available_cash()
b.new_cash()
c = SBI()
c.available_cash()
c.sbicash()'''

#multiple inheritance

'''class Father():
    def weight(self):
        print("70 kgs")
class Mother():
    def height(self):
        print("5.5 inches")
class Kid():
    def DoB(self):
        print("Just born . . . . .")
a = Father()
a.weight()
b = Mother()
b.height()
c = Kid()
c.DoB()'''


'''class Father():
    def weight(self):
        print("70 kgs")
class Mother():
    def height(self):
        print("5.5 inches")
class Kid(Mother,Father):
    def DoB(self):
        print("Just born . . . . .")

c = Kid()
c.weight()
c.height()
c.DoB()'''

#multi level inheritance
'''class Grandparent():
    def land(self):
        print("land is 100 acres")
class Parents(Grandparent):
    def house(self):
        print("apartments")
class Child(Parents):
    def bike(self):
        print("Honda bike")

a = Child()
a.land()
a.house()
a.bike()'''

































































    

































    
