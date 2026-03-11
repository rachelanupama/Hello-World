Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#negative striding
a = 'python course'
a[-1:-8:-3]
'eu '
a[::-1]
'esruoc nohtyp'
a[::2]
'pto ore'
a[:9]
'python co'

#string methods
#len()
a = 'rachel'
len(a)
6
b = 'python course'
len(b)
13
a= ''
len(a)
0
a= ' '
len(a)
1
#count()
a = 'twinkle twinkle little star'
a.count(twinkle)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.count(twinkle)
NameError: name 'twinkle' is not defined
a.count('twinkle')
2
a.count('t')
5
a.count('s')
1
a.count(' ')
3
a.count('o')
0

#find a string
a = 'python'
a[1]
'y'
a.find('n')
5
b = 'anupama'
b.find('a')
0
b[0]+b[4]+b[6]
'aaa'

#escape sequesnces
#escape sequences
# \n new line
#\t tab space

a='name\nmobleno\tmailid\ncity"
SyntaxError: unterminated string literal (detected at line 1)
KeyboardInterrupt
a='name\nmobleno\tmailid\ncity'
print(a)
name
mobleno	mailid
city
a='name: Rachel\nmobleno: 1234567\tmailid: rachel@123\ncity:Guntur'
print(a)
name: Rachel
mobleno: 1234567	mailid: rachel@123
city:Guntur
a='name: Rachel\nmobileno: 1234567\tmailid: rachel@123\ncity:Guntur'
print(a)
name: Rachel
mobileno: 1234567	mailid: rachel@123
city:Guntur

#replace
a = "wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b = "wait...wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b.replace("wait","work")
'work...work until you succeed'
b.replace("wait","work",2)
'work...work until you succeed'
b.replace("work","wait",2)
'wait...wait until you succeed'
b.replace("work","wait",1)
'wait...wait until you succeed'

a = "hello"
#upper()
a.upper()
'HELLO'
b = "HII"
#lower
b.lower()
'hii'
c = 'python'
c.capitalize()
'Python'
c = "i am learning pythom"
c.capitalize()
'I am learning pythom'
c.title()
'I Am Learning Pythom'

a = 'code'
a.isupper()
False
a.islower()
True
a.startswith('c')
True
a.endswith('e')
True
a.isalpha()
True
b = 'python course'
b.isalpha()
False
b.isdigit()
False
c = 4567
c.isdigit()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    c.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
c = "4567"
c.isdigit()
True
c = 'rachel1234'
c.isalnum()
True
c = 'rachel@123'
c.isalnum()
False

#strip()
#lstrip(), rstrip()
a = "                 python              "
a.strip()
'python'
a.lstrip()
'python              '
a.rstrip()
'                 python'

#split()

a = "python java c c++"
a.split()
['python', 'java', 'c', 'c++']
a = 'I am Rachel Anupama'
a.split()
['I', 'am', 'Rachel', 'Anupama']

#join()
a = "python", "java", "c", "c++"
''.split(a)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    ''.split(a)
TypeError: must be str or None, not tuple
''.join(a)
'pythonjavacc++'
' '.join(a)
'python java c c++'
'*'.join(a)
'python*java*c*c++'

#concatenation
a = 'code'
b = 'gnan'
print(a+b)
codegnan
a = 'python'
b = 'course'
print(a+' '+b)
python course
print (a.title() +' '+b.tile())
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    print (a.title() +' '+b.tile())
AttributeError: 'str' object has no attribute 'tile'. Did you mean: 'title'?
print (a.title() +' '+b.title())
Python Course
print((a+' '+b),title())
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    print((a+' '+b),title())
NameError: name 'title' is not defined. Did you mean: 'tuple'?
print((a+' '+b).title())
Python Course

#formatting
a=8
b=7
print(a+b)
15
print("the sum is",a+b)
the sum is 15
a = "rachel"
print("my name is",a)
my name is rachel

#format method
a = 'motu'
b = 'patlu'
print("hello {} {}",format(a,b))
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    print("hello {} {}",format(a,b))
ValueError: Invalid format specifier 'patlu' for object of type 'str'
print("hello {} {}".format(a,b))
hello motu patlu
print("hello {} !! hello {} !!".format(a,b))
hello motu !! hello patlu !!

#fstring
a = 'sita'
b = 'ram'
print(f"hello {a} {b})
      
SyntaxError: unterminated f-string literal (detected at line 1)
print(f"hello {a} {b}")
      
hello sita ram
print (f"hello {b} !! hello {a} !!")
      
hello ram !! hello sita !!
a = 'sita'
      
#lists
      
a [3,5.6,"python", 9+8j, True, False]
      
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    a [3,5.6,"python", 9+8j, True, False]
TypeError: string indices must be integers, not 'tuple'
a = [3,5.6,"python", 9+8j, True, False]
      
a
      
[3, 5.6, 'python', (9+8j), True, False]
type(a)
      
<class 'list'>
a.append("o")
      
a
      
[3, 5.6, 'python', (9+8j), True, False, 'o']
a.append(["Java", "c"])
      
a
      
[3, 5.6, 'python', (9+8j), True, False, 'o', ['Java', 'c']]
a.extend(["css","22"])
      
a
      
[3, 5.6, 'python', (9+8j), True, False, 'o', ['Java', 'c'], 'css', '22']
#insert()
      
a.insert(3, "dsa")
      
a
      
[3, 5.6, 'python', 'dsa', (9+8j), True, False, 'o', ['Java', 'c'], 'css', '22']
[3, 5.6, 'python', 'dsa', (9+8j), True, False, 'o', ['Java', 'c'], 'css', '22']
      
[3, 5.6, 'python', 'dsa', (9+8j), True, False, 'o', ['Java', 'c'], 'css', '22']

a = ["apple", "mango", "orange"]
      
a.index("mango")
      
1
a.copy()
      
['apple', 'mango', 'orange']
b = a.copy()
      
b
      
['apple', 'mango', 'orange']
['apple', 'mango', 'orange']
      
['apple', 'mango', 'orange']
b.clear()
      
b
      
[]
b.append("hello")
      
b
      
['hello']
b.extend(["hi","anyways"])
      
b
      
['hello', 'hi', 'anyways']
#pop
      
a = ["hi","hello","u"]
      
a
      
['hi', 'hello', 'u']
a.pop()
      
'u'
a
      
['hi', 'hello']
a.pop(0)
      
'hi'
#sort
      
a = ['w','e','t','e','h']
      
a.sort()
      
a
      
['e', 'e', 'h', 't', 'w']
a =[4,6,2,9,0,1,4]
      
a.sort()
      
a
      
[0, 1, 2, 4, 4, 6, 9]
#reverse
      
a.reverse()
      

a
      
[9, 6, 4, 4, 2, 1, 0]
 b=['white','blue','orange','red']
      
SyntaxError: unexpected indent
b=['white','blue','orange','red']
      
b.reverse()
      
b
      
['red', 'orange', 'blue', 'white']

#remove
      
a.remove("4")
      
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    a.remove("4")
ValueError: list.remove(x): x not in list
>>> b.remove("white")
...       
>>> b
...       
['red', 'orange', 'blue']
>>> 
>>> a = ["mango","dragon","kiwi"]
...       
>>> len(a)
...       
3
>>> b = "mango"
...       
>>> len(b)
...       
5
>>> c = ["mango"]
...       
>>> len(c)
...       
1
>>> c.count()
...       
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    c.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> c.count("mango")
...       
1
