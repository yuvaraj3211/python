class library:
    def __init__(self):
        self.a=[]
        self.members=[]
    def addbooks(self,b):
        self.a.extend(i.strip() for i in b.split(','))
    def displaybooks(self):
        for i in self.a:
            print(i)
    def addmember(self,name):
        m=Member(name)
        self.members.append(m)
        print(f"Member {name} added")
    def findmember(self,name):
        for i in self.members:
            if i.name==name:
                return i
        return None
    def search(self,book):
        if book in self.a:
            print(f"{book} book is available")
        else:
            print(f"{book} book is not available")
    def issue_book(self,bookname,membername):
        m=self.findmember(membername)
        if m is None:
            print("Member not found")
            return
        if bookname not in self.a:
            print("Book not available")
            return
        self.a.remove(bookname)
        m.books_issued.append(bookname)
        print(f"{bookname} issued to {membername}")
    def returnbook(self,bookname,membername):
        m=self.findmember(membername)
        if m is None:
            print("Member not found")
            return
        if bookname not in m.books_issued:
            print("This member hasnt issued that book")
            return
        m.books_issued.remove(bookname)
        self.a.append(bookname)
        print(f"{bookname} returned successfully")
    def show_member_details(self,membername):
        m=self.findmember(membername)
        if m is None:
            print("Meber not found")
            return
        print(f"Name: {m.name}")
        print(f"Books issued: {m.books_issued}")
class Member:
    def __init__(self,name):
        self.name=name
        self.books_issued=[]
print('''options: 
    option 1: Add books
    option 2: Display books
    option 3: search the books
    option 4: adding member
    option 5: isuue a book
    option 6: return a book
    option 7: member details
    option 8: Exit
    ''')
x=library()
while True: 
    opt=input('select the option: ')
    if opt=='1':
        x.addbooks(input("enter the books you want (separated by commas): "))
    elif opt=='2':
        print("the available books are:")
        x.displaybooks()
    elif opt=='3':
        book=input('enter the book u want to search: ')
        x.search(book)
    elif opt=='4':
        x.addmember(input('enter member name: '))
    elif opt=='5':
        b=input("enter book name to issue: ")
        n=input("enter member name: ")
        x.issue_book(b,n)
    elif opt=='6':
        b=input('enter book name to return: ')
        n=input('enter meber name: ')
        x.returnbook(b,n)
    elif opt=='7':
        n=input("enter member name: ")
        x.show_member_details(n)
    elif opt=='8':
        break
