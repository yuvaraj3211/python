Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #sets{}
>>> a=
SyntaxError: invalid syntax
>>> a={4,7.8,"yuvaraj",5+9j,True,False}
>>> print(a)
{False, True, (5+9j), 4, 'yuvaraj', 7.8}
>>> type(a)
<class 'set'>
>>> b={7,8,9,5,7,6}
>>> print(b)
{5, 6, 7, 8, 9}
>>> 
>>> #add
>>> 
>>> a={4,5,6,7,8,9}
>>> a.add(15)
>>> a
{4, 5, 6, 7, 8, 9, 15}
>>> 
>>> #issubset()
>>> 
>>> a={3,4,5,6,7,8,9}
>>> b={6,7,8,9}
>>> b.issubset(a)
True
>>> a.issubset(b)
False
>>> 
>>> #superset()
>>> 
>>> a={5,6,7,8,9,10,11}
>>> b={7,8,9,10}
>>> a.issuperset(b)
True
>>> b.superset(a)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    b.superset(a)
AttributeError: 'set' object has no attribute 'superset'. Did you mean: 'issuperset'?
>>> b.issuperset(a)
False
>>> 
>>> #union
>>> 
>>> a={3,4,5,6,7}
b={1,2,3,4,5,6,7,8}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}
b.union(a)
{1, 2, 3, 4, 5, 6, 7, 8}

#intersection

a={3,4,5,6,7}
b={1,2,3,7,8,9}
a.intersection(b)
{3, 7}
b.intersection(a)
{3, 7}

#difference()

a={7,8,9,10,11,12,13}
b={8,9,10,11,12,13,14,15}
a.difference(b)
{7}
b.difference(a)
{14, 15}

#update()

a={2,3,4,5,6}
b={1,4,5,6,7,8,9}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}

#symmetric_difference()

a={2,3,4,5,6,7,8}
b={1,4,6,8,9,10,11}
a.symmetric_difference(b)
{1, 2, 3, 5, 7, 9, 10, 11}

#difference_update()

a={4,5,6,7,8,9}
b={1,2,3,4,5,6,10}
a.difference_update(b)
a
{7, 8, 9}
b.difference_update(a)
b
{1, 2, 3, 4, 5, 6, 10}

#intersection_update()

a={3,4,5,6,7,8}
b={5,6,7,8,9,10}
a.intersection_update(b)
a
{8, 5, 6, 7}
b.intersection_update(a)
b
{8, 5, 6, 7}

#symmetric_difference_update

a={11,12,13,14,15,16}
b={13,14,15,16,17,18}
a.symmetric_difference_update(b)
a
{17, 18, 11, 12}
b.symmetric_difference_update(a)
b
{16, 11, 12, 13, 14, 15}

#pop and remove

a={3,4,5,6,7,8}
a.pop()
3
a
{4, 5, 6, 7, 8}
a.pop(2)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a.pop(2)
TypeError: set.pop() takes no arguments (1 given)
a.remove(6)
a
{4, 5, 7, 8}
print(a.remove(6))
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    print(a.remove(6))
KeyError: 6

#copy discard clear

a={10,20,30,40,50}
a.copy()
{50, 20, 40, 10, 30}
b=a.copy()
b
{50, 20, 40, 10, 30}

a.discard(50)
a
{20, 40, 10, 30}

a={10,20,30,40,50}
a.clear()
a
set()
b=set()
b.add(100)
b
{100}

#isdisjoint()

a={2,3,4,5,6}
b={6,7,8,9,10}
a.isdisjoint(b)
False

c={10,20,30,40}
d={50,60,70,80}
c.isdisjoint(d)
True
