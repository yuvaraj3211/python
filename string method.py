Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#strings
#len()

a="codegnan"
len(a)
8
b="python course"
len(b)
13
c=""
len(d)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    len(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
c=""
len(c)
0
d=" "
len(d)
1
e="i am in vijayawada"
len(e)
18


#count
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("k")
2
a.count("t")
5
a.count(" ")
3
a.count("")
28


#find a string
a="python"
a[1]
'y'
a.find("h")
3
b="hello"
a.find(3)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.find(3)
TypeError: find() argument 1 must be str, not int
a.find(l)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.find(l)
NameError: name 'l' is not defined
a.find("l")
-1
c="hello"
a.find("l")
-1
c.find("l")
2


#escape sequences
#\n -> new line
#\t -> tab space

a="name\mailid\tmobileno\ncollege\tbranch"
print(a)
name\mailid	mobileno
college	branch
a="name\nmailid\tmobileno\ncollege\tbranch"
print(a)
name
mailid	mobileno
college	branch
b="name:yuvaraj\nmailid:rekapalliyuvaraj8@gmail.com\tmobileno:9390066819\ncollege:pvpsit\tbranch:ece"
print(b)
name:yuvaraj
mailid:rekapalliyuvaraj8@gmail.com	mobileno:9390066819
college:pvpsit	branch:ece


#replace()
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="python java"
a.replace("p","c")
'wait until you succeed'
b.replace("p","c")
'cython java'
c="wait wait until you succeed"
c.replace("wait","work")
'work work until you succeed'
c.replace("wait","work",1)
'work wait until you succeed'


#upper
a="code"
a.upper()
'CODE'

#lower
a="HELLO"
a.lower()
'hello'

#capitalize
a="python"
a.capitalize()
'Python'
a="python course"
a.capitalize()
'Python course'

#tittle
a="i am in class"
a.tittle()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a.tittle()
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
a.title()
'I Am In Class'
a="python course"
a.title()
'Python Course'


#using is
a="code"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
b="code course"
b.isalpha()
False
c="codecourse"
c.isalpha()
True
d=1234
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d="12341"
d.isdigit()
True
a="yuvaraj123"
a.alnum()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a.alnum()
AttributeError: 'str' object has no attribute 'alnum'. Did you mean: 'isalnum'?
a.isalnum()
True
a="yuvaraj@123"
a.isalnum()
False
a="yuvaraj,123"
a.isalnum()
False


#startswith and endswith
a="data science"
a.startswith("d")
True
a.endswith("e")
True
b="yuvaray"
b.startswith("y")
True


#strip
#lstrip,rstrip
a="     yuvaraj      "
a.strip()
'yuvaraj'
a.lstrip()
'yuvaraj      '
a.rstrip()
'     yuvaraj'
b="i am"
b.strip()
'i am'
b="i am yuvaraj"
b.lstrip()
'i am yuvaraj'


#split()-----print seperate
a="python java c++ c"
a.split()
['python', 'java', 'c++', 'c']
b="i love python"
b.split()
['i', 'love', 'python']


#join()
b="html","css","js"
b="html","css","js","bs"
"".join(b)
'htmlcssjsbs'
" ".join(b)
'html css js bs'
"k".join(b)
'htmlkcsskjskbs'
c="python"
" ".join(c)
'p y t h o n'
",".join(c)
'p,y,t,h,o,n'


#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
a="python course"
b="by python"
print(a+b)
python courseby python
fname="yuvaraj"
lname="rekapalli"
print(fname+lname)
yuvarajrekapalli
print(fname+" "+lname)
yuvaraj rekapalli
print(fname.title()+" "+lname.title())
Yuvaraj Rekapalli
print((fname+" "+lname).title())
Yuvaraj Rekapalli


#formatting
a=5
b=7
print(a+b)
12
print("the sum is",a+b)
the sum is 12
city="vijayawada"
print("the city is",city)
the city is vijayawada
>>> print("the sum is,a+b)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> 
>>> #format
...       
>>> a="motu"
...       
>>> b="pathlu"
...       
>>> print("hello {}{}".format(a,b))
...       
hello motupathlu
>>> print("hello {} {}".format(a,b))
...       
hello motu pathlu
>>> print("hello {} {}".format(a,b))
...       
hello motu pathlu
>>> print("hello {}\nhello {}".format(a,b))
...       
hello motu
hello pathlu
>>> 
>>> 
>>> #fstring
...       
>>> a="sita"
...       
>>> b="ram"
...       
>>> print(f"hello {a}{b}")
...       
hello sitaram
>>> print(f"hello {a} {b}")
...       
hello sita ram
>>> print(f"hello {a} hello {b}")
...       
hello sita hello ram
>>> print(f"hello {a}\nhello {b}")
...       
hello sita
hello ram
