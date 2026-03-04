Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthemantic

a=3
b=7
a+b
10
a +=b
a
10
a+12
22
b/=11
a+b
10.636363636363637
a/b
15.714285714285715
a
10
b
0.6363636363636364
b+=a
b
10.636363636363637
a+b
20.636363636363637
b //=a
b
1.0
a+b
11.0
b -=a
b
-9.0
#comparision
r= 8
s = 7
r<=s
False
r>=s
True
s<=s
True
s,+r
(7, 8)
(7, 8)
(7, 8)


a! =b
SyntaxError: invalid syntax
r != s
True
a==b
False
a>b
True
a<b
False
#logical
a<b and b>a
False
a<= b and b==a
False
a! =b or b<a
SyntaxError: invalid syntax
a != b pr b<a
SyntaxError: invalid syntax
a != b or b<a
True
not True
False
not False
True

#identify operators
if type(a) is int :
    print("it is int")

    
it is int
if type(b) is not float :
    print(" it is not float")

    
if type(a) is not str:
    print("it is not str")

    
it is not str
it is not str
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    it is not str
NameError: name 'it' is not defined. Did you mean: 'id'?


#membership
p = 1,2,3,4,5,7,8
if 8 in a:
    print (True)

    
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    if 8 in a:
TypeError: argument of type 'int' is not a container or iterable
if 8 in p:
    print(True)

    
True
if 6 in p;
SyntaxError: invalid syntax
if 6 in p:
    print(False)

    


if 6 in p:
    print(False)
... 
...     
>>> a=2
>>> b=3
>>> a&b
2
>>> bin (a)
'0b10'
>>> bin(b)
'0b11'
>>> # for and, 1 = 1,1
>>> # for 1, at least one 1 = 1
>>> a = 9
>>> b=3
>>> a|b
11
>>> #or
>>> 
>>> 

... 
>>> 

>>> #xor (^) only opposite is 1
>>> #xor (^) only opposite is 1
>>> a = 8
>>> b = 7
>>> a^b
15
>>> a = 6
>>> 9= 4
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> e=7
>>> a^e
1
