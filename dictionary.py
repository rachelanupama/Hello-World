Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============= RESTART: C:/Users/Lydia/Desktop/python/march/loops.py ============
CODEGNAN PYTHON COURSE 
#dictionary

a = {"name" : "rachel", "city" : "guntur"}
type (a)
<class 'dict'>
a.keys()
dict_keys(['name', 'city'])
a.values()
dict_values(['rachel', 'guntur'])
a.items()
dict_items([('name', 'rachel'), ('city', 'guntur')])

#update
a.update({"date" : "14th"})
a
{'name': 'rachel', 'city': 'guntur', 'date': '14th'}
a.update({"time" : "12:30 am", {"day":"saturday"})
         
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
a.update({"time" : "12:30 am"}, {"day":"saturday"})
         
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.update({"time" : "12:30 am"}, {"day":"saturday"})
TypeError: update expected at most 1 argument, got 2
a.update({"time" : "12:30 am","day":"saturday"})
         
a
         
{'name': 'rachel', 'city': 'guntur', 'date': '14th', 'time': '12:30 am', 'day': 'saturday'}
a.setdefault("year",2026)
         
2026
a
         
{'name': 'rachel', 'city': 'guntur', 'date': '14th', 'time': '12:30 am', 'day': 'saturday', 'year': 2026}
a.setdeault(2026,"year")
         
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.setdeault(2026,"year")
AttributeError: 'dict' object has no attribute 'setdeault'. Did you mean: 'setdefault'?
a.setdefault(2026,"year")
         
'year'
a
         
{'name': 'rachel', 'city': 'guntur', 'date': '14th', 'time': '12:30 am', 'day': 'saturday', 'year': 2026, 2026: 'year'}
a.pop()
         
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("name")
         
'rachel'
a
         
{'city': 'guntur', 'date': '14th', 'time': '12:30 am', 'day': 'saturday', 'year': 2026, 2026: 'year'}
a.popitem()
         
(2026, 'year')
a
         
{'city': 'guntur', 'date': '14th', 'time': '12:30 am', 'day': 'saturday', 'year': 2026}
a.copy()
         
{'city': 'guntur', 'date': '14th', 'time': '12:30 am', 'day': 'saturday', 'year': 2026}
a
         
{'city': 'guntur', 'date': '14th', 'time': '12:30 am', 'day': 'saturday', 'year': 2026}
a.get("name")
         

a.get("city")
         
'guntur'
a.clear()
         
a
         
{}
a = {"name" : "rachel", "city" : "guntur", "name" : "rachel"}
         
a
         
{'name': 'rachel', 'city': 'guntur'}
a.count()
         
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.count()
AttributeError: 'dict' object has no attribute 'count'
a.index("name")
...          
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.index("name")
AttributeError: 'dict' object has no attribute 'index'
>>> a = {"name" : "rachel", "city" : "guntur", "name" : "rachel", "name" : "anupama"}
...          
>>> a
...          
{'name': 'anupama', 'city': 'guntur'}
>>> a = {"name" : "rachel", "city" : "guntur", "name1" : "rachel", "name2" : "anupama"}
...          
>>> a
...          
{'name': 'rachel', 'city': 'guntur', 'name1': 'rachel', 'name2': 'anupama'}
>>> a {"idnos" : [10,11,12], "names" :['sita','priya','rani'}
...    
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a {"idnos" : [10,11,12], "names" :['sita','priya','rani'}
...    a= {"idnos" : [10,11,12], "names" :['sita','priya','rani']}
...    
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a ={"idnos" : [10,11,12], "names" :['sita','priya','rani'}
...     
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a= {"idnos" : [10,11,12], "names" :['sita','priya','rani']}
...     
>>> a
...     
{'idnos': [10, 11, 12], 'names': ['sita', 'priya', 'rani']}
