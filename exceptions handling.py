#EXCEPTION HANDLING()

#try->instructions from which we are expecting the exceptions
#except->exceptions are raised in try block it will be handle by this block
#else->no exceptions(optional)
#finally->always it will display

'''while True:
    try:
        a=int(input("a value"))
        b=int(input("b value"))
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptions")
    finally:
        print("program ends........")'''

#FILE HANDLING

#write

'''a=open("yuvaraj.txt","w")
b=a.write("python full stack")
a.close()'''

'''a=open("yuvaraj.txt","w")
b=a.write("codegnan it solutions")
a.close()'''

#append()

'''a=open("yuvaraj.txt","a")
b=a.write("\tyuvaraj")
a.close()'''

'''a=open("yuvaraj.txt","a")
b=a.write(input("enter the text"))
a.close()'''

'''n=input()
a=open("yuvaraj.txt","a")
b=a.write(n)
a.close()'''

'''a=open("yuvaraj.txt","w")
n=input()
b=a.write(n)
a.close()'''

'''a=open("yuvaraj.txt","w")
n=input()
b=a.write(n)
a.close()'''

#readlines

'''a=open("yuvaraj.txt")'''
#print(a.read())#it will display entire content
#print(a.readline())#it will display first line
#print(a.readlines())#it will display in list with \n
#print(a.read(7))#it will display no of characters

#writelines()->it makes evry object side by side

'''a=open("raja.txt","w")
b=["sandeep","sai","vasu","roop","srinadh"]
a.writelines("\n".join(b))
a.close()'''

'''a=open("conditions.py")
print(a.read())'''

'''a=open("C:\\Users\\rekap\\OneDrive\\Desktop\\yrpython\\sets.py")
print(a.read())'''

























