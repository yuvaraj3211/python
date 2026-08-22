#functions

#a fuction is a block of organized,reusable code and that is used to perform a single or multiple task
#python gives inbuilt function like print(),u can make ur own function also and these are user defined functions
#function blocks begin with a keyword def followed by the function name and paranthesis()

'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

'''a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

'''a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

#functions

'''def calculator(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculator(10,20)
calculator(100,200)
calculator(1000,2000)'''

'''def calculator(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
x=int(input())
y=int(input())
calculator(x,y)'''

'''def calculator(a,b):
    print("the power is",a**b)
    print("the module is",a%b)
    print("the int division is",a//b)
calculator(2,3)'''

'''def even(a):
    if a%2==0:
        print("even")
even(2)'''

'''def add(a,b):
    print(a+b)
add(5,7)'''

'''while True:
    def add():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    add()'''

'''def add():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
    add()
add()'''

#difference between print vs return

#print just shows the human user output in a console
#return is a keyword and return is used to terminate the function and gives back a value from the function

'''def mul(a,b):
    print(a*b)
mul(4,5)'''

'''def mul(a,b):
    return a*b
print(mul(4,6))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(4,5)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(4,5))'''

'''while True:
    def add():
        a=int(input("enter a value"))
        b=int(input("enter b value"))
        print(a+b)
    def sub():
        a=int(input("enter a value"))
        b=int(input("enter b value"))
        print(a-b)
    def mul():
        a=int(input("enter a value"))
        b=int(input("enter b value"))
        print(a*b)
    options=int(input(''''''))
    print(f"the option is{options}")
    if option==1:
            print(a+b)
    elif option==2:
            print(a-b)
    elif option==3:
            print(a*b)'''

while True:
    def calculate():
        a=int(input("a value"))
        b=int(input("b value"))
        c=a+b
        d=a-b
        e=a*b
        option=int(input('''choose the option
                                  1.add
                                  2.sub
                                  3.mul'''))
        if option==1:
            print(c)
        elif option==2:
            print(d)
        elif option==3:
            print(e)
    calculate()

#split bill
    




    





















    

