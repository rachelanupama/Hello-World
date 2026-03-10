Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#striding
a ='data science'
a[::]
'data science'
a[::1]
'data science'
a[::3]
'dacn'
a[::-1]
'ecneics atad'
a[::-3]
'eest'

b = 'machine learning'
a[::4]
'd e'
a[3:9]
'a scie'
a[::6]
'dc'
b[::4]
'miln'
a[3:9]
'a scie'
b[3:9]
'hine l'
>>> a[::6]
'dc'
>>> b[::6]
'men'
>>> b[::9]
'me'
>>> b[::7]
'm n'
>>> b[::2]
'mcielann'
>>> a[5:]
'science'
>>> b[5:]
'ne learning'
>>> a[::4]
'd e'
>>> b[::4]
'miln'
>>> b[::8]
'ml'
>>> a='cloud computing'
>>> a[1:7:2]
'lu '
>>> a='cloud computing'
>>> a[2:14:3]
'o mt'
>>> a[5:10:3]
' m'
>>> a[3:12:4]
'uot'
