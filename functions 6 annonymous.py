#annonymous functions
#annonymous are name less fuctions and we use a keyword called as LAMBDA to create annonymous functions

#write a function to calculate 2*x+5 where x=5

'''def calculate():
    x=5
    y=2*x+5
    print(y)
calculate()'''

'''def f(x):
    print(2*x+5)
f(5)

def f():
    x=int(input("value"))
    print(2*x+5)
f()'''

#syntax
#a=lambda arg:expr

'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input())
b=lambda x:2*x+5
print(b(a))'''

'''a="codegnan" #CODEGNAN
b=lambda x:x.upper()
print(b(a))

b=lambda a:a.upper()
print(b("codegnan"))

a="python course" #Python Course
b=lambda a:a.title()
print(b(a))'''

'''a=5;b=10
c=lambda x:a*b
print(c(a))

a=int(input())
b=int(input())
c=lambda x:a*b
print(c(a))'''

'''a=lambda x,y:x*y
print(a(2,4))'''

'''x=int(input())
y=int(input())
c=lambda x,y:x*y
print(c(x,y))'''

'''a=input()
b=input()
c=lambda a,b:a+b
print(c(a,b))'''

'''a="yuva"
b="raj"
c=lambda x:a+b
print(c(a))'''

'''fname,lname=input().split()
c=lambda fname,lname:fname+lname
print(c(fname,lname))'''

'''a,b=[x for x in input("enter the names").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

#filter
#a=[10,20,30,50,60,80,25,73,100]

'''if a%2==0:
    print(a)'''

'''for i in a:
    if i%2==0:
        print(i)'''

'''b=list(filter(lambda x:x%2==0,a))
print(b)'''

#[],(),{}

'''a=[]
print(type(a))

b=()
print(type(b))

c={}
print(type(c))

d=set()
print(type(d))'''

'''a=[[],(),set(),{}," ",None,3,5.6,"python",7+9j,True,False]
b=list(filter(None,a))
print(b)'''

#map()->each object from a collection and forms a new

'''a=[2,5,7,9,10,20,30,80]
b=[1,9,20,50,60,4,25,80]
c=list(map(max(a,b))
print(c)
d=list(map(min(a,b))
print(d)'''



















