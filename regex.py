#regex (regular expressions) ---> R.E are powerful tools(module) embedded in python which is maily used to find a pattern within a given string or statements or file.
# we mainly use it for text manipulation

'''a = "the tree  is tall"
print(a)'''

'''a = "the\ntree\nis\ttall"
print(a)'''

#rstring - raw string

'''a = r"the\ntree\nis\ttall"
print(a)'''

#complle(), search (), findall(), split(), sub()
#sequence charcaters
'''
\w -  it matches alpahanumeric
\W - it matches non alphanumeric
\d -   it matches any digit
\D -  it matches non digit
\s -   it matches white spaces
\S -   it matches non white spaces'''

import re
a = "map cat map maths cash monkey money donkey cap dog"
'''b = re.compile(r"m\w\w\w\w")
print(b)

c = b.search(a)
print(c)

d = re.search(r"m\w+",a)
print(d)'''

#findall()
'''e = re.findall(r"m\w+",a)
print(e)
print(*e)'''

'''x = re.split(r"m\w+",a)
print(x)'''

'''y = re.split(r"\s",a)
print(y)'''

'''z = re.sub(r"monkey","lion",a)
print(z)'''


b = "1,2,3,4,5, rachel"
c = re.findall(r"\d+",b)
print(c)
e = re.findall(r"\D+e",b)
print(e)































































