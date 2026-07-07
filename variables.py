Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
print(6+8)
14
a=2
b=3
print(a+b)
5
a=0,1,2,3,4,5,6,7,8,9
print(a)
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
x=50
print(x)
50
name="yuvaraj"
print(name)
yuvaraj
2=30
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a2=30
print(a2)
30
4a=60
SyntaxError: invalid decimal literal
a0123456789=100
print(a0123456789)
100
#special characters
@=50
SyntaxError: invalid syntax
$=70
SyntaxError: invalid syntax
_=30

_=30
print(_)
30
_d=20
print(_d)
20
#does not allow any keywords
if=60
SyntaxError: invalid syntax
first name="yuvaraj"
SyntaxError: invalid syntax
first_name="yuvaraj"
print(first_name)
yuvaraj
firstname="yuvaraj'
SyntaxError: unterminated string literal (detected at line 1)
firstname="yuvaraj"
print(firstname)
yuvaraj
#single in two variables separated with semi colomns
a=4,b=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=4;b=9
print(a+b)
13
a,b=4,9
print(a+b)
13
a=2,3,4,5,6,7,8,9
print(a)
(2, 3, 4, 5, 6, 7, 8, 9)
a,b,c=1,2,3
print(a,b.c)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(a,b.c)
AttributeError: 'int' object has no attribute 'c'
a,b,c=1,2,3
print(a,b,c)
1 2 3
>>> a,b,c=23457
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a,b,c=23457
TypeError: cannot unpack non-iterable int object
>>> a,b,c=(6,7,8)
>>> print(a,b,c)
6 7 8
>>> #delete keyword
>>> a=6
>>> print(a)
6
>>> del a
>>> print(A)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(A)
NameError: name 'A' is not defined
>>> fname="yuvaraj")
SyntaxError: unmatched ')'
>>> fname="yuvaraj"
>>> lname"rekapalli"
SyntaxError: invalid syntax
>>> fname="yuvaraj"
>>> lname="rekapalli"
>>> print(fname+lname)
yuvarajrekapalli
>>> print(fname+ lname)
yuvarajrekapalli
>>> print(fname+" "+lname)
yuvaraj rekapalli
>>> print(fname,lname)
yuvaraj rekapalli
>>> print(lname+" "+fname)
rekapalli yuvaraj
>>> #case sensitive
>>> name="yuvaraj"
>>> print(name)
yuvaraj
>>> NAME="yuvaraj"
>>> print(NAME)
yuvaraj
>>> Name="yuvaraj"
>>> print(Name)
yuvaraj
