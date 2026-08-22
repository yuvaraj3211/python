#regex(regular expressions)
#regular expressions are powerfull tools(module embeded in python which is mainly used to find a pattern with in a given string
#or statements or files and we mainly use it for text manupulations

'''a="codegnan is in vja"
print(a)'''

'''a="codegnan\nis\tin\nvja"
print(a)'''

#rstring

'''a=r"codegnan\nis\t\nvja"
print(a)'''

#compile(), search(), findall(), split(), sub
#sequence characters

'''\w->it matches alphanumeric
\W->it matches non-alpha numeric
\d->it matches any digit
\D->it matches non digit
\s->it represents white spaces
\S->it represents non-white spaces'''

#compile()

import re
a="map maths cat code cash money mat cup cap monkey"
'''b=re.compile(r"m\w\w\w\w\w")
print(b)'''

#search()

'''c=b.search(a)
print(c)'''

'''b=re.search(r"m\w+",a)
print(b)'''

#findall

'''c=re.findall(r"m\w+",a)
print(*c)'''

'''import re
a="map maths cat code cash money mat cup cap monkey"
b=re.compile(r"c\w\w\w")
c=b.search(a)
print(c)'''

#split()

'''d=re.split(r"m",a)
print(d)

e=re.split(r"\S",a)
print(e)

f=re.split(r"\s",a)
print(f)'''

#sub()

'''g=re.sub(r"m","a",a)
print(g)'''

'''import re
a="a12 b345 c67 d89'"
b=re.findall(r"\d+",a)
print(b)

import re
a="year 2026 month 8 date 6"
b=re.findall(r"\d+",a)
print(b)'''

#error handling

'''1.syntax error->compile error
2.run time error->during execution time it will happens
3.logical error->error in logic(it can't be vivible)'''

#syntax error

'''for i in range(20)
print(i)'''

#run time error

'''a=int(input("a value"))
b=int(input("b value"))
print(a//b)''' #10//0->zero dividion error

#logical error

'''a=10
b=20
print(a-b)'''

'''a=10
b=2
if a<b:
    print("true")'''


















