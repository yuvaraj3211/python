#oops
#syntax

'''class classname():
    #attributes
    name="pooja"
    age=28
    place="vja"
    def fname(metod_name):
        print("statements...............")
a=classname()
print(dir(a))
a.fname()'''

#class declaration

'''class Details():
    name="pooja"
    age=28
    place="vja"
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

#object instantiation

'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("yuvaraj",20,"vja")
a.display()'''

'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("yuvaraj",20,"vja")
a.display()
b=Details()
b.data("xyzaraj",20,"vja")
b.display()
c=Details()
c.data("abcraj",20,"vja")
c.display()'''

#object initialization

'''class data():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=data("mango",22,"vja")
print(dir(a))
a.display()'''

#user input

'''class data():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=input()
b=int(input())
c=input()
x=data(a,b,c)
print(dir(x))
x.display()'''

'''class data():
    #creating a constructor
    def __init__(self):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=data()
print(dir(a))
a.display()'''

'''class data():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=data(input("name"),int(input("age")),input("place"))
print(dir(a))
a.display()'''


#14 august

#diff blw _ and __
#when user want to create a variable in python by using __ underscore our python interpreter treats it as special variable to avoid name conflicts with methods and inner classes

'''class Employee():
    def __init__(self):
        self.name="pooja"  #public
        self._mailid="pooja@codegnan.com"  #protected
        self.__salary=10000  #private variable
a=Employee()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Employee__salary)

class Employee1():
    def __init__(self):
        self.name="yuvaraj"  #public
        self._mailid="yuvaraj@gmail.com"  #protected
        self.__salary=10000  #private variable
a=Employee1()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Employee1__salary)'''


#polymorphism

#operator overloading

'''a=4;b=8
print(a+b)
print(a.__add__(b))
print(a.__sub__(2))
print(a.__mul__(6))
print(a.__pow__(2))
#print(a.__div__(4))
print(a.__eq__(4))
print(a.__le__(8))
print(a.__ge__(10))
a=[1,2,3,4,5];b=[6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(4))
a="code";b="gnan"
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b).title())'''

#operator overriding

'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(6)
y=B(4)
#x=6
#y=4
print(x+y)'''

#method overloading

'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("product is",a*b)
        else:
            print("program ends......")
a=new()
#a.sum()
#a.sum(3,6,8)
a.sum(4,5)'''

#method overriding

'''class Animal():
    def speak(self):
        print("animal can make sounds")
class Dog():
    def speak(self):
        print("dog can barks")
a=Animal()
b=Dog()
a.speak()
b.speak()'''

#task

'''class car():
    def vehicle(self):
        print("thar")
class bike():
    def vehicle(self):
        print("vespa")
a=car()
b=bike()
a.vehicle()
b.vehicle()'''


#17-8-2026

#inheriance

#single inheritance

'''class rbi():#parent class
    cash=100000
    def available_cash(cls):
        #print("available cash is",cls.cash)
        print("available cash is",rbi.cash)
class sbi(rbi):#child-1
    pass
class hdfc(rbi):#child-2
    cash=50000
    def new_cash(cls):
        #print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+rbi.cash)
a=hdfc()
a.available_cash()
a.new_cash()'''

#multiple inhertance

'''class father():
    def height(self):
        print("height is",175)
class mother():
    def weight(self):
        print("weight is",60)
class child(father,mother):
    def dob(self):
        print("dob is",'19-10-2005')
a=child()
a.height()
a.weight()
a.dob()'''

#multilevel

'''class grandparent():
    def land(self):
        print("land is ",'1acre')
class parent(grandparent):
    def house(self):
        print("house is",'100sqft')
class child(parent):
    def bike(self):
        print("the bike is",'pulsur')
a=child()
a.land()
a.house()
a.bike()'''

#hierarchical inheritance
#def: hierarchical inheritance is one parent class is inheritant by multiple child classes

'''class employee():
    def company(self):
        print("company name is nagainfotech")
class trainer(employee):
    def teaching(self):
        print("the teaching is rider")
class developer(employee):
    def develop(self):
        print("the developer is anish")
a=trainer()
a.teaching()
a.company()
b=developer()
b.develop()
b.company()'''

#hybrid inheritance

#def hybrid inheritance means combining one or more than one type of inheritance for example multiple and multilevel and alse hierarchical + multiple

'''class person():
    def details(self):
        print("the person is rohith")
class trainer(person):
    def teaching(self):
        print("the trainer is raider")
class student(person):
    def learning(self):
        print("the student is anish")
class programmanager(trainer,student):
    def manage(self):
        print("the program manager is nagaraj")
a=programmanager()
a.details()
a.teaching()
a.learning()
a.manage()'''



#18-8-2026

#super()

'''class parent():#super class
    def __init__(self,name):
        self.name=name
        print("parent consructor")
class child(parent):#sub class
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
        print("child constructor")
a=child("yuvaraj",20)
print(a.age)
print(a.name)'''

#ENCAPSULATION

#combine multiple units into single unit is known it as a encapsulation
#it have three types

#public data

'''class a():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class b(a):
    def method2(self):
        print(self.publicdata)
obj1=b()
obj1.method1()
obj1.method2()'''

#protect data

'''class a():
    _protecteddata=10
    def method1(self):
        print(self._protecteddata)
class b(a):
    def method2(self):
        print(self._protecteddata)
obj1=b()
obj1.method1()
obj1.method2()
print(obj1._protecteddata)'''

#__privatedata

'''class a():
    __privatedata="yuvaraj"
    def method1(self):
        print(self.__privatedata)
class b(a):
    def method2(self):
        print(self._a__privatedata)
obj1=b()
obj1.method1()
obj1.method2()'''


# 19-08-2026


#abstraction

#hiding unnecessary informationfrom user is called abstration
#it is two types 1.abstract class 2.abstract method

#abstract class
#one or more abstract method is called abstract class

#abstract method
#the method is declared without implementation is called abstract method

'''class a():
    def method1(self):
        pass
obj1=a()
obj1.method1()'''

'''class a():
    def method1(self):
        print("data")
obj1=a()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class a(ABC):
    @abstractmethod
    def method1(self):
        print("data science")
obj1=a()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class A():
    def method1(self):
        print("python course")
obj1=A()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class A(ABC):#parent class
    def method1(self):
        pass
    def method2(self):
        print("python full stack")
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("data structures")
    def method3(self):
        print("java full stack")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()'''




































































