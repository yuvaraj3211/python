Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes conversions
#int
int(4)
4
int(8.9)
8
print("hi")
hi
int("hi")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(5+9j)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(5+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(true)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(false)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    int(false)
NameError: name 'false' is not defined. Did you mean: 'False'?

#float
float(7)
7.0
float(5.6)
5.6
float("hello")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float("hello")
ValueError: could not convert string to float: 'hello'
float(5.9j)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    float(5.9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
>>> 
>>> #string
>>> str(5)
'5'
>>> str(7.8)
'7.8'
>>> str("string")
'string'
>>> str(5.9j)
'5.9j'
>>> str(True)
'True'
>>> str(False)
'False'
>>> 
>>> #comple
>>> complex(1)
(1+0j)
>>> complex(1.1)
(1.1+0j)
>>> complex("yuvaraj")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    complex("yuvaraj")
ValueError: complex() arg is a malformed string
>>> complex(5+9j)
(5+9j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> 
>>> #bool
>>> bool(8)
True
>>> bool(8.1)
True
>>> bool("yuvaraj")
True
>>> bool(5+9j)
True
>>> bool(True)
True
>>> bool(False)
False
