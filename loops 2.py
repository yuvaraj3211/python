#difference between break,continue,pass
#break is used to terminate the entire loop
#continue is used to skips the current iteration and rest of the code will continue
#pass is a null statement it does nothing but syntatically we need

#break

'''a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break'''

'''a=20
while a>3:
    a=a-1
    if a==6:
        break
    print(a)'''

'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''

'''a="yuvaraj rekapalli"
for i in a:
    if i=="e":
        break
    print(i)'''

#continue

'''a=30
while a>5:
    print(a)
    a=a-1
    if a==15:
        continue'''

'''a=30
while a>5:
    a=a-1
    if a==15:
        continue
    print(a)'''

'''for i in range(15):
    if i==11:
        continue
    print(i)'''

'''a="python"
for i in a:
    if i=="h":
        continue
    print(i)'''

#pass

'''a=9
while a>2:
    print(a)
    a=a-1
    if a==7:
        pass'''

'''for i in range(25):
    if i==20:
        pass
    print(i)'''

#ATM APPLICATION

'''a=int(input("account: "))
p=int(input("password: "))
card=input("card: ")
if card=='c':
    print("welcome yuvaraj")
else:
    print("invalid")
if p==1234:
    print("correct password")
else:
    print("invalid password")
n=int(input(f"enter options: {"1.balance"} {"2.withdraw"}"))
b=int(input("account balance: "))
if b=='a':
      print("account balance is",b)
w=int(input("withdraw:"))
z=b-w
print("remaining balance: ",z)'''

#correct code

while True:
    account=100000
    pwd=1234
    card=input("insert the card")
    if card=="c":
        print("welcome pooja")
        password=int(input("enter the password"))
        if password==pwd:
            option=int(input('''choose the option 1.balance enq  2.withdraw'''))
            if option==1:
                print("acc bal is",account)
            elif option==2:
                money=int(input("enter the ammount"))
                print(money)
                balance=account-money
                print("rem acc bal is",balance)
            else:
                print("invalid option")
        else:
            print("incorrect password")
    else:
        print("invalid card")
                                          
          




















    

