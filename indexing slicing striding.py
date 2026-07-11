Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
#positive indexing
a="i am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[2]+a[3]
'am'
a[5]+a[6]
'in'
a[1]+a[4]+a[7]
'   '
a="12345"
a[0]
'1'
a123456
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a123456
NameError: name 'a123456' is not defined
a=12345
a[1]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a[1]
TypeError: 'int' object is not subscriptable
a= i am learning python
SyntaxError: invalid syntax
a="i am learning python"
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
a[5]+a[6]+a[7]+a[8]+a[9]
'learn'
a=
SyntaxError: invalid syntax
a="i love codegnan"
a[7]+a[8]+a[9]+a[10]
'code'
a[11]+a[12]+a[13]+a[14]
'gnan'
a[2]+a[3]+a[4]+a[5]
'love'
b="vijayawada is a royal city"
b[-10]+b[-9]+b[-8]+b[-7]+b[-6]
'royal'
b[-4]+b[-3]+b[-2]+b[-1]
'city'
b[-15]+b[-16]
'i '
b[-15]+b[-14]
'is'
a="vizag is a city of destiny"
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'destiny'
a[-15]+a[-14]+a[-13]+a[-12]
'city'

a[-26]+a[-25]+a[-24]+a[-23]+a[-22]
'vizag'
print(a[-26]+a[-25]+a[-24]+a[-23]+a[-22])
vizag


#slicing

a="codegnan
SyntaxError: unterminated string literal (detected at line 1)
a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a="work until you succeed"
a[0:4]
'work'
a[5:10]
'until'
a[11:14]
'you'
a[15:21]
'succee'
a[15:22]
'succeed'
>>> a="time is very precious"
>>> a[13:21]
'precious'
>>> a[8:12]
'very'
>>> a[0:3]
'tim'
>>> a[0:4]
'time'
>>> a[:4]
'time'
>>> a[13:]
'precious'
>>> b="simple is better than complex"
>>> b[-19:-13]
'better'
>>> b[-29:-23]
'simple'
>>> b[-7:-1]
'comple'
>>> b[-7:]
'complex'
>>> b[-7:0]
''
>>> b="codegnan it solutions"
>>> b[-21:-13]
'codegnan'
>>> b[-9:]
'solutions'
>>> b[-9:1]
''
>>> b[-9:]
'solutions'
>>> b[-9:-1]
'solution'
>>> 
>>> #striding
>>> a="data science"
>>> a[::]
'data science'
>>> a[::!]
SyntaxError: invalid syntax
>>> a[::1]
'data science'
>>> a[::2]
'dt cec'
