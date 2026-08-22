#print()

'''a=2
b=3
c=a+b
print(c)

#input()

a=input()
print(a)

#max()

a=[1,2,3,4,5]
b=max(a)
print(b)

#min()

b=[1,2,3,4,5]
a=min(b)
print(a)

#sum()

a=[1,2,3,4,5]
b=sum(a)
print(b)

#len()

a=[1,2,3,4,5]
b=len(a)
print(b)

#type()

a=(1,2,3,4,5)
b=type(a)
print(b)

#range()

n=6
for i in range(n):
    print(i)

#pow()

a=2
b=pow(a)
print(b)'''

#fromkeys()

'''a="codegnan"
print(a)

print(list(a))

print(tuple(a))

print(set(a))'''

#print(dict(a))

'''b=dict.fromkeys(a)
print(b)
c=dict.fromkeys(a,"pooja")
print(c)

c["o"]="python"
print(c)'''

#eval()

'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''

'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

'''while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''

#zip()->we can combine multiple collections into one collection

'''a=[10,20,30,40,50,60]
names=["sowmya","priya","kavya","preethi","harika"]
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

c=tuple(zip(a,names))
print(c)

c=set(zip(a,names))
print(c)

c=dict(zip(a,names))
print(c)

d=list(zip(a,names))
print(*d)'''

#enumurate()->we can give counter to the collection

'''names=["hemanth","vasu","roop","sai","spider"]
for i in range(len(names)):
    print(i,names[i])'''

'''b=dict(enumerate(names))
print(b)'''

'''b=dict(enumerate(names,100))
print(b)'''

#railway ticket

'''while True:
    def railway():
        n=int(input("the ticket price: "))
        a=input("gender is male or female:")
        b=int(input("age: "))
        if a=="male" and b>=60:
            t=n-30/100*n
            print("the ticket price is",t)
        elif a=="male" and b<60:
            print("no discount the ticket price is",n)
        elif a=="female" and b>=60:
            s=n-50/100*n
            print("the ticket price is",s)
        elif a=="female" and b<60:
            p=n-30/100*n
            print("the ticket price is",p)
    railway()'''



























