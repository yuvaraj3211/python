Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,4.5,"python",6+9j,True,False]
print(a)
[2, 4.5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=8.9
type(b)
<class 'float'>
c=[8.9]
type(c)
<class 'list'>

#append()
a["python","c","c++]
  
SyntaxError: unterminated string literal (detected at line 1)
a=["python","c","c++]
   
SyntaxError: unterminated string literal (detected at line 1)
a=["python","c","c++"]
   
a.append("java")
   
a
   
['python', 'c', 'c++', 'java']
a.append("html","css")
   
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.append("html","css")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["html","css"])
   
a
   
['python', 'c', 'c++', 'java', ['html', 'css']]

#extend()
   
a=["html","css","js"]
   
a.extend(["python","java"])
   
a
   
['html', 'css', 'js', 'python', 'java']

#insert()
   
b=["vja","hyd","vzg"]
   
b.insert(1,"chennai")
   
b
   
['vja', 'chennai', 'hyd', 'vzg']

a=["apple","banana","grapes"]
   
a.index("grapes")
   
2
a.copy()
   
['apple', 'banana', 'grapes']
b=a.copy()
   
b
   
['apple', 'banana', 'grapes']

a.count("apple")
   
1

len(a)
   
3

d="apple"
   
len(d)
   
5

e=["apple"]
   
len(e)
   
1

#sort
   
a=["mango","kiwi","dragon","berry"]
   
a.sort()
   
a
   
['berry', 'dragon', 'kiwi', 'mango']

b=[9,3,7,0,49,23,5,6,24]
   
b.sort()
   
b
   
[0, 3, 5, 6, 7, 9, 23, 24, 49]

#reverse()
   
a=["ds","ai","ml"]
   
a.reverse()
   
a
   
['ml', 'ai', 'ds']

b=[5,7,8,3,4,5]
   
b.reverse()
   
b
   
[5, 4, 3, 8, 7, 5]

#pop and remove
   
a=["black","white","red","blue","pink"]
   
a.pop()
   
'pink'
a
   
['black', 'white', 'red', 'blue']

a.pop(2)
   
'red'

a
   
['black', 'white', 'blue']
a.pop("black")
   
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.pop("black")
TypeError: 'str' object cannot be interpreted as an integer
>>> a=["black","white","red","blue","pink"]
...    
>>> a.remove("black")
...    
>>> a
...    
['white', 'red', 'blue', 'pink']
>>> 
>>> #clear
...    
>>> a=["ap","ts","ka"]
...    
>>> a.clear()
...    
>>> a
...    
[]
>>> b=[]
...    
>>> a.append("pooja")
...    
>>> b
...    
[]
>>> 
>>> 
>>> #tuple()
...    
>>> a=(4,6.7,"python",8+9j,True,False)
...    
>>> print(a)
...    
(4, 6.7, 'python', (8+9j), True, False)
>>> type(a)
...    
<class 'tuple'>
>>> a.index(8+9j)
...    
3
>>> len(a)
...    
6
>>> a.count(True)
...    
1
