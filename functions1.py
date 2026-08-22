#splitbill()

'''def splitbill():
    a=int(input("enter the no of friends"))
    b=int(input("enter the amount"))
    print("per head bill is",b//a)
splitbill()'''

'''def splitbill():
    a=int(input("enter the no of friends"))
    b=int(input("enter the amount"))
    print(f"per head bill is {b//a}")
    print(f"per head bill is {}".format(b//a))    
splitbill()'''

'''def splitbill():
    a=int(input("enter the no of friends"))
    b=int(input("enter the amount"))
    print(f"per head bill is {c}")
    print(f"per head bill is {}".format(c))    
splitbill()'''

#keyword and positional arguements

'''def details(id,name,mailid):
    id=10
    name="pooja"
    mailid="pooja@codegnan.com"
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")'''

'''def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
details(id=20,name="malvika",mailid="m@gmail.com")
details(id=30,name="lohitha",mailid="l@gmail.com")
details(40,"geethika","m@gmail.com")
details("teja","t@gmail.com",50)
details(name="barani",mailid="b@gmail.com",id=60)'''

#default arguements

'''def grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("rice",1500)'''

'''def grocery(item="sugar",price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery()'''

'''def grocery(item,price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("dhal")'''

'''def grocery(item="ghee",price):
    #non def arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery(500)'''

#cake,price,quantity

'''def raj(cake,price,quantity):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
raj("chocolate",400,"1kg")'''

'''def raj(cake="chocolate",price=400,quantity="1kg"):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
raj()'''

'''def raj(cake,price=400,quantity="1kg"):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
raj("chocolate")'''

'''def raj(cake="chocolate",price,quantity="1kg"):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
raj(400)'''

# * arguements(* is used to umpack the elements)

'''a=[10,20,30,40,50]
print(a)
print(*a)'''

'''a=(10,20,30,40,50)
print(a)
print(*a)'''

'''a={10,20,30,40,50}
print(a)
print(*a)'''

'''a={"year":2026,"month":"july"}
print(a)
print(*a)'''

'''a,b,c=2,3,4,5,6,7,8,9,0
print(a)
print(b)
print(c)'''

'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''a,*b,c=2,3,4,5,6,7,8,9,0
print(a)
print(*b)
print(c)'''

'''a="codegnan"
print(a)
print(*a)'''

'''a="codegnan"
print(a)
print(b)
print(c)'''

'''a,b,c="code"
print(a)
print(b)
print(c)'''

'''a,b,*c=2,3,4,5,6,7,8,9,0
print(a)
print(b)
print(*c)'''





















