Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=5
type(a)
<class 'int'>
b=7.8
print(b)
7.8
c='code'
print(c)
code
b=7.8
type(b)
<class 'float'>
>>> c='code'
>>> typr(c)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    typr(c)
NameError: name 'typr' is not defined. Did you mean: 'type'?
>>> c='code'
>>> type(c)
<class 'str'>
>>> d="codegnan"
>>> type(d)
<class 'str'>
>>> e='''python'''
>>> type(e)
<class 'str'>
>>> f="c"
>>> typr(f)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    typr(f)
NameError: name 'typr' is not defined. Did you mean: 'type'?
>>> f="c"
>>> type(f)
<class 'str'>
>>> x=5+9J
>>> type(x)
<class 'complex'>
>>> y=3j+7
>>> type(y)
<class 'complex'>
>>> z=6j
>>> type(z)
<class 'complex'>
>>> b="j"
>>> type(b)
<class 'str'>
>>> a=6+8i
SyntaxError: invalid decimal literal
>>> type(a)
<class 'int'>
>>> c=True
>>> type(c)
<class 'bool'>
>>> d=False
>>> type(d)
<class 'bool'>
