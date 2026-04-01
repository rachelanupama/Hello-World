Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#math module
import math
math.pi
3.141592653589793
math.pi*7
21.991148575128552
math.sqrt(16)
4.0
math.log(10)
2.302585092994046
math.sin(30)
-0.9880316240928618
math.tan(42)
2.2913879924374863
math.cos(60)
-0.9524129804151563
math.pow(2,4)
16.0
math.ceil(5.9)
6
math.ceil(4.8)
5
math.floor(3.5)
3
math.floor(2.1)
2

from math import pi,log,sqrt,pow
pi
3.141592653589793
log(10)
2.302585092994046
math.pi
3.141592653589793
pow(1,3)
1.0
#system module
import sys
sys.path
['', 'C:\\Program Files\\Python314\\Lib\\idlelib', 'C:\\Program Files\\Python314\\python314.zip', 'C:\\Program Files\\Python314\\DLLs', 'C:\\Program Files\\Python314\\Lib', 'C:\\Program Files\\Python314', 'C:\\Users\\Lydia\\AppData\\Roaming\\Python\\Python314\\site-packages', 'C:\\Program Files\\Python314\\Lib\\site-packages']
for i in sys.path:
    print(i)

...     

C:\Program Files\Python314\Lib\idlelib
C:\Program Files\Python314\python314.zip
C:\Program Files\Python314\DLLs
C:\Program Files\Python314\Lib
C:\Program Files\Python314
C:\Users\Lydia\AppData\Roaming\Python\Python314\site-packages
C:\Program Files\Python314\Lib\site-packages
>>> sys.version
'3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)]'
>>> #os module
>>> import os
>>> os.path
<module 'ntpath' (frozen)>
>>> os.getcwd()
'C:\\Program Files\\Python314'
>>> os.listdir()
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python314.dll', 'pythonw.exe', 'Scripts', 'tcl', 'vcruntime140.dll', 'vcruntime140_1.dll']
>>> os.mkdir("1ST")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    os.mkdir("1ST")
PermissionError: [WinError 5] Access is denied: '1ST'
>>> os.mkdir("first")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    os.mkdir("first")
PermissionError: [WinError 5] Access is denied: 'first'
