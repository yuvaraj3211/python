#variable length arguements
#variable length arguements automatically stores in tuple and we use star arguements

'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7)
b=[4,5,6,7,8]
check(*b)
c={6,7,8,9,10}
check(*c)
d={"name":"pooja","scity":"vja"}
check(*d)'''

'''def check1(*a):
    d=2#creating a variable
    print(a)
    print(type(a))
    for i in a:
        d=d+i
        print(d)
check1()
check1(2,3,4,5,6,7)
check1(1,3,4,5.2,3.4)
check1(3,4,2,5,3.6,2.4,"pooja")'''

'''def check1(*a):
    d=2#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
           d=d+i
           print(d)
check1()
check1(2,3,4,5,6,7)
check1(1,3,4,5.2,3.4)
check1(3,4,2,5,3.6,2.4,"pooja")'''

#kwargs(**)

'''def check(**a):
    print(a)
    print(type(a))
check()
details={"idnos":[10,20,30],"names":["sai","siva","ravi"],"status":["p","a","p"]}
check(**details)'''

'''def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check()
details={"idnos":[10,20,30],
         "names":["sai","siva","ravi"],
         "status":["p","a","p"]}
check(**details)'''

#both * and ** usage

'''def final(*a,**b):
    d=3#creating a variable
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,3.5,6.2)
final(*data)
details={"idnos":[10,20,30],
         "names":["sai","siva","ravi"],
         "status":["p","a","p"]}
final(**details)
final(*data,**details)'''

#max(),min(),sum()

'''print(max(5,7,9,10,20,40))
print(min(5,7,9,10,20,40))

a=[5,7,9,10,20,40]
b=sum(a)
print(b)'''

#students marks analysis

'''n=int(input("enter no of students"))
a=[]
for i in range(1,n+1):
    b=int(input(f"enter the {i} student marks"))
    a.append(b)
for i in marks:
    print(i)
print("----attendence report----")
c=max(a)
print("maximum value is: ",c)
d=min(a)
print("minimum value is: ",d)
e=sum(a)
print("the sum is: ",e)
f=e/n
print("the average is: ",f)'''






















