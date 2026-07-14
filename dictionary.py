SPython 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={"name":"pooja","year":2026,"month":7}
print(a)
{'name': 'pooja', 'year': 2026, 'month': 7}
type(a)
<class 'dict'>

a.keys()
dict_keys(['name', 'year', 'month'])

a.values()
dict_values(['pooja', 2026, 7])

a.items()
dict_items([('name', 'pooja'), ('year', 2026), ('month', 7)])

#update()

a={"year":2026,"month":"july","date":14}
a.update({"time":2})
a
{'year': 2026, 'month': 'july', 'date': 14, 'time': 2}
a.update({"time":2},{"day":"true"})
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.update({"time":2},{"day":"true"})
TypeError: update expected at most 1 argument, got 2
a
{'year': 2026, 'month': 'july', 'date': 14, 'time': 2}
a.update({"time":2,"day":"true"})
a
{'year': 2026, 'month': 'july', 'date': 14, 'time': 2, 'day': 'true'}

#setdefault()

a={"name":"yuvaraj","city":"vja"}
a.setdefault("mail","rekapalliyuvaraj8@gmail.com")
'rekapalliyuvaraj8@gmail.com'
a
{'name': 'yuvaraj', 'city': 'vja', 'mail': 'rekapalliyuvaraj8@gmail.com'}

#pop()

a={"state":"ap","country":"india"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a={"state":"ap","country":"india"}
a.pop("country")
'india'
a
{'state': 'ap'}

#popitem()

a={"state":"ap","country":"india"}
a.popitem()
('country', 'india')
a
{'state': 'ap'}

#copy and len

a={"colour":"black","food":"biriyani"}
a.copy()
{'colour': 'black', 'food': 'biriyani'}
b=a.copy()
b
{'colour': 'black', 'food': 'biriyani'}

>>> len(a)
2
>>> 
>>> a={"name":"pooja","city":"vja","name":"pooja"}
>>> print(a)
{'name': 'pooja', 'city': 'vja'}
>>> a={"name":"pooja","city":"vja","name":"priya"}
>>> a
{'name': 'priya', 'city': 'vja'}
>>> a={"name1":"pooja","city":"vja","name2":"pooja"}
>>> a
{'name1': 'pooja', 'city': 'vja', 'name2': 'pooja'}
>>> 
>>> a.count("name1")
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a.count("name1")
AttributeError: 'dict' object has no attribute 'count'
>>> a.index("city")
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.index("city")
AttributeError: 'dict' object has no attribute 'index'
>>> 
>>> #clear and update
>>> 
>>> a={"name":"pooja","city":"vja","name":"pooja"}
>>> a.clear()
>>> a
{}
>>> b={}
>>> b.update({"name":"yuvaraj"})
>>> b
{'name': 'yuvaraj'}
>>> 
>>> a={"idnos":[10,20,30],"names":["sai","kiran","basha"],"marks":[60,70,80]}
>>> print(a)
{'idnos': [10, 20, 30], 'names': ['sai', 'kiran', 'basha'], 'marks': [60, 70, 80]}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idnos', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['sai', 'kiran', 'basha'], [60, 70, 80]])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['sai', 'kiran', 'basha']), ('marks', [60, 70, 80])])
