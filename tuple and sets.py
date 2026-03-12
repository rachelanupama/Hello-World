Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple
a = (2,4.5,"c",7+9j,True,False)
type(a)
<class 'tuple'>
len(a)
6
a.index(True)
4
a,count(4.5)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a,count(4.5)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count(4.5)
1
sets()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    sets()
NameError: name 'sets' is not defined. Did you mean: 'set'?
#sets()
a = {2,3.4,"rachel",9+9j,True}
a
{True, 2, 3.4, (9+9j), 'rachel'}
b ={5,6,7,8,9}
b
{5, 6, 7, 8, 9}
type(b)
<class 'set'>
a.add(0)
a
{0, True, 2, 3.4, (9+9j), 'rachel'}
a = {1,2,3,4,5}
b = {3,4,5}
a.issubset(b)
False
b.issubset(a)
True
a = {3,4,5,6,7,8}
b ={7,8,9,0}
a.issubset(a)
True

#union()
a = {1,2,3,4,5,6}
b = {4,5,6,7,8}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}

a,intersection(b)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a,intersection(b)
NameError: name 'intersection' is not defined
NameError: name 'intersection' is not defined
SyntaxError: invalid syntax
a.intersection(b)
{4, 5, 6}
{4, 5, 6}
{4, 5, 6}
a = {2,3,4,5,6}
b = {2,3,7,8,9}
a.difference(b)
{4, 5, 6}
b.difference(a)
{8, 9, 7}
c = {2,1,3,4,6,5,7,9,8}
a.update(c)
c
{1, 2, 3, 4, 5, 6, 7, 8, 9}
c.update(b)
a.difference_update(b)
a
{1, 4, 5, 6}
a = {2,3,4,5,6,7}
b = {1,2,3,4,5,6,7,8,9}
a.difference_update(b)
a
set()
b.difference_update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a = {2,1,3,0}
b.difference_update(a)
b
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8, 9}a.symmetric_difference(b)
SyntaxError: invalid syntax
a.symmetric_difference(b)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
b.symmetric_difference(a)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
a = {10,20,30,40}
b = {30,40,50,60}
a.symmetric_difference_update(b)
a
{10, 50, 20, 60}
b.symmetric_difference_update(a)
b
{40, 10, 20, 30}
a = {2,3,4,5,6}
b = {3,4,5,6,7,8,9}
a.pop()
2
b.pop()
3
a.remove(5)
a
{3, 4, 6}
a,copy()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a,copy()
NameError: name 'copy' is not defined. Did you forget to import 'copy'?
>>> a.copy()
{3, 4, 6}
>>> a.clear()
>>> a.add(19)
>>> a
{19}
>>> b = set()
>>> b.add(77)
>>> b
{77}
>>> 
>>> b.discard(77)
>>> b
set()
>>> len(b)
0
>>> #n index and no count
>>> 
>>> a = {2,3}
>>> b = {3,4}
>>> a.isdisjoint(b)
False
>>> a = {3,4,5}
>>> b = {6,7,8}
>>> a.isdisjoint(b)
True
>>> 
>>> #dictionary
>>> 
