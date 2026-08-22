#goblal and local variables

#a variable is defined above the fuction and is accessible to the entire global space is called global variables
#a variable is defined inside the function is called local variables

#first case of global variable

'''a=2
def check1():
    print("the inside value is",a)
check1()
print("outside vakue is",a)'''

#second case of global variable

'''a=4
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("outside value is",b)'''

#third case of both global and local variables

'''a=3
b=8
def check3():
    a=6
    prit("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=12#local variable
    b=b+a
    print("value of b is",b)
check3()
print("a value is",a)
print("b value is",b)'''

#usage of global keyword

#when user wants to create a variable inside the function directly and carry forward the updated value then we need to use global keyword

'''a=4
def final():
    global a,b
    print("inside value is",a)
    a=15
    print("updated value is",a)
    b=20
    b=b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)'''

#genrators

#no tuple comprehension in above cases if remove those graces and key paranthesis and then the outcome is generators

#a=[expr for var in collection/range]

'''a=[i for i in range(16)]
print(a)
print(type(a))'''

'''a=(i for i in range(16))
print(*a)
print(type(a))'''

'''a=(i for i in range(16))
#print(list(a))
#print(tuple(a))
print(set(a))'''

#a generator is also a function which can be used as an iterator (loop) by producing group of values and we can use "yeild" keyword
#yield vs return
#return will terminate the function where as yield can pass the function and go on with every successive iteration

'''a,b=(int(x) for x in input ("values").split(","))
def check(a,b):
    while a<b:
        #yield a
        a=a+1
        yield a
print(*check(a,b))'''

'''a,b=(int(x) for x in input ("values").split(","))
def check(a,b):
    while a<b:
        a=a+1
        #return a
    return a
print(check(a,b))'''

#yield vs return

'''def mygen():
    #return 'vja"
    #return "hyd"
    #return "vzg"
    return "vja","hyd","vzg"
print(*mygen())'''

'''def mygen():
    yield "python"
    yield "java"
    yield "c"
print(*mygen())'''

#next()
'''d=mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))#stop iteration'''
























    
