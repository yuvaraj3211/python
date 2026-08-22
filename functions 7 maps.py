#map

'''a=input("data1")
b=input("data2")
print(a+b)'''

'''a,b=input("enter the data").split(",")
print(a+b)

a,b=[x for x in input("enter the names").split(",")]
print(a+b)

a,b=map(str,input("enter the data").split(","))
print(a+b)

a=int(input("a value"))
b=int(input("b value"))
print(a+b)

a,b=[int(x) for x in input("enter the values").split(",")]
print(a+b)

a,b=int(input("enter the values").split(","))
print(a+b) #error

a,b=map(int,input("enter the values").split(","))
print(a+b)'''

'''a=list(map(int,input("values").split(",")))
print(a)
print(type(a))

a=tuple(map(int,input("values").split(",")))
print(a)
print(type(a))

a=set(map(int,input("values").split(",")))
print(a)
print(type(a))'''

'''a=input("enter the key and value")
b=dict(i.split(":") for i in a.split(","))
print(b)'''

'''a=list(map(eval,input("values").split(",")))
print(a)
print(type(a))'''

#difference between module, library and package

#module:
#a module i python in single python file it consist python code
#examples of modules include math.py, random.py, mymodule.py
#it contains functions, class and variables

#package:
#one or more modules python modules and an __init__.py file
#examples of packages include requests, numpy, pandas

#library:
#it consist both modules and packages
#examples of library such as numpy,pandas,matplotlib

#note:
#a python file is a module and input is keyword and every python file is saved internally with variable name as __main__

#module

'''import rypython
rypython.greetings("yuvaraj")'''

'''import rypython'''

'''import rypython'''

#math module

'''import math
print (math.pi)
print (math.pi*3)
print (math.sqrt(2))
print (math.pow(2,4))
print (math.log(2))
print (math.tan(45))
print (math.sin(60))
print (math.cos(30))
print (math.ceil(2.9))
print (math.ceil(5.9))
print (math.ceil(8))
print (math.floor(2.7))'''

'''from math import pi,log,sqrt
print(pi)
print(log(10))
print(sqrt(2))'''

#sys module

'''import sys
print(sys.path)
print(sys.version)'''

#os module

'''import os'''
'''print(os.path)
print(os.getcwd())
print(os.listdir())
print(os.mkdir("aug 4"))
print(os.listdir())'''

'''print(os.chdir("C:\\Users\\rekap\\Downloads"))
print(os.listdir())'''

#ASCII

'''print(chr(67))

print(chr(65))

print(chr(90))

print(chr(93))

print(ord("a"))

print(ord("z"))

#print(ord(97)) #error

print(chr(97))'''

'''for i in range(97,123):
    print(chr(i),end=" ")'''

'''for j in range(65,91):
    print(chr(j),end=" ")'''

'''a=input("enter a string: ")
for i in a:
    print(i,"-",ord(i))'''

    



























