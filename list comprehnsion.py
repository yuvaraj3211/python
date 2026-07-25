#list comprehension
#every list comprehension can be written as a for loop but every for loop cannot be rewritten in list comprehension

'a=["python","java","dsa"]'
#["PYTHON","JAVA","DSA"]
#print(a.upper())error

'''b.str(a)
print(b.upper())'''

'''for i in a:
print(i.upper(),end=" ")'''

#syntax

#=[expr for var in collection/range]

'''a=[i.upper() for i in a]
print(a)'''

'''a=["codegnan","course","python"]
b=[i.title() for i in a]
print(b)'''

'''a=[1,3,4,5,6,8,12,13]
b=[i*i for i in a]
b=[i**2 for in in a]
b=[poe(1,2) for i in a]
print(b)'''

#if usage in list comprehension

'''a=[i for i in range(21) if i%2==0]
print(a)'''


'''a=[i for i in range(21) if i%2!=0]
print(a)'''

'''a=[i*i for i in range(21) if i%2==0]
print(a)'''

'''a=["apple","banana","mango","dragon","kiwi","berry"]
b=[i for i in a if "a" in i ]
print(b)'''

'''a=["apple","banana","mango","dragon","kiwi","berry"]
b=[i for i in a if "a" not in i ]
print(b)'''

#no elif usage in list comprehension

#range(16)

'''a=[i**2 if i%2==0 else i*5 for i in range(16)]
print(a)'''

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]'''
#[6,6,6,6,6]

'''c=[a[i]+a[j] for i in range(len(a)) for j in range(len(b)) if a[i]+a[j]==6]
print(c)'''

'''c=[a[i]+b[i] for i in range(len(a))]
c=[a[i]+b[i] for i in range(5)]
print(c)'''

#attendence report

'''while True:
    a=int(input("enter no of students: "))
    p=0
    e=0
    for i in range(1,a+1):
         n=input(f"enter the student details {i}: ")
         if n=="p":
                p=p+1
    e=a-p
    print("total students: ",a)
    print("presenties: ",p)
    print("absenties: ",e)'''


























