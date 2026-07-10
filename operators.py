Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #operators
>>> #airthmetic operators
>>> a=2
>>> b=4
>>> peinr(a+b)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    peinr(a+b)
NameError: name 'peinr' is not defined. Did you mean: 'print'?
>>> print(a+)
SyntaxError: invalid syntax
>>> print(a+b)
6
>>> print(a-b)
-2
>>> print(a*b)
8
>>> print(a**b)
16
>>> print(a//b)
0
>>> print(a/b)
0.5
>>> print(a%b)
2
>>> #assignment operators
>>> a=3
>>> b=5
>>> print(a+=b)
SyntaxError: invalid syntax
>>> a+=b
>>> a
8
>>> a-=3
>>> a
5
>>> a*=b
>>> a
25
>>> a**=2
>>> a
625
>>> a//=2
>>> a
312
a/=4
a
78.0
a%=4
a
2.0
a=a+b
a
7.0
b+=2
b
7
b-=2
b
5
b*=2
b
10
b**=2
b
100
b//=2
b
50
b/=2
b
25.0
b%=2
b
1.0
#comparision operator
a=6
b=8
print(a<b)
True
b>a
True
a<=b
True
b>=a
True
a!=b
True
a=b
a==b
True
a=7
b=9
a==b
False
#logical operators
a=4
b=8
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a!=b or a==b
True
not true
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not True
False
not False
True
1.0
1.0

#identify operators
a=6
type(a) is int
True
type(a) is not int
False
b=6.7
type(b) is float
True
type(b) is not float
False
c="yuvaraj"
type(c) is string
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    type(c) is string
NameError: name 'string' is not defined. Did you forget to import 'string'?
c="yuvaraj'
SyntaxError: unterminated string literal (detected at line 1)
c="yuvaraj"
type(c) is String
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    type(c) is String
NameError: name 'String' is not defined
c='yuvaraj'
type(c) is String
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    type(c) is String
NameError: name 'String' is not defined
c="yuvaraj"
type(c) is str
True
type(c) is not str
False
d=3+1j
type(d) is complex
True
type(d) is not complex
False
#membership operators
a=2,3,4,5,6,7,8,9
9 in a
True
10 in a
False
10 in not a
SyntaxError: invalid syntax
10 not in a
True
print(10 not in a)
True
b="python
SyntaxError: unterminated string literal (detected at line 1)

b="python","java","c"
c in b
False
d not in b
True
c not in b
True
#bitwise operator
a=4
b=6
a&b
4
bin(4)
'0b100'
bin(6)
'0b110'
a=7
b=9
bin(7)
'0b111'
bin(9)
'0b1001'
a&b
1
a=5
b=9
bin(5)
'0b101'
bin(9)
'0b1001'
a|b
13
a=2
b=6
bin(a)
'0b10'
bin(b)
'0b110'
a|b
6
a=6
-(a+1)
-7
~a
-7
b=12
~b
-13
c=-9
~c
8
a=2
b=3
a^b
1
a=3
b=4
bin(a)
'0b11'
bin(b)
'0b100'
a^b
7
a=4
a<<2
16
a=3
a>>3
0
