import showBooks
import list2d
import borrowBook
import returnBook
import record
import record2dlist 
import borrowreturncheck as b
import bill
list3 = []
list4=[]

firstname = input("Enter first name:").upper()
lastname = input("Enter last name:").upper()
fullname = firstname+' '+ lastname
try:
    if fullname==int:
        answer= True
        print("Invalid Entry")
a = 'y'
while a == 'y':
    list1 = []
    list2 = []
    list2d.list2d(list1)
    record2dlist.record2dlist(list2)
    answer = True
    while (answer == True):
        types = input("Enter 1 to borrow a book\nEnter 2 to return the book\n")
        if types == '1' or types =='2':
            answer = False
        else:
            print("Invalid!\nEnter again.\n")
    answer = True
    showBooks.showBooks(list1)
    if types == '1':
            while (answer == True):
                try:
                    snumber = int(input("Enter the serial number to borrow a book"))
                    if int(snumber)>0 and int(snumber)<len(list1):
                        answer = False
                    else:
                        print("Invalid!\nEnter again.\n")
                except:
                    print("Invalid!\nEnter again.\n")
                    print(list1[snumber][3])
            if int(list1[snumber][3]) >= 1:
                an = b.recordborrow(list1,list2,fullname,snumber)
                if an == True:
                    list3.append(int(snumber))
                    borrowBooks = borrowBook.borrowBook(list1,snumber)
                    print("Book has been borrowed")
                    records = record.record(fullname,list1,types,snumber)
            else:
                print("The item is out of stock")
    else:
        while (answer == True):
            try:
                snumber = input("Enter the serial number to return the book")
                if int(snumber)>0 and int(snumber)<len(list1):
                    answer = False
                else:
                    print("Invalid!\nEnter again.\n")
            except:
                print("Invalid!\nEnter again.\n")

            an,a = b.recordreturn(list1,list2,fullname,snumber,list4)
            if an == True:
                if int(snumber) in list3:
                    list3.remove(int(snumber))
                returnBook.returnBook(list1,snumber)
                print("The book has been returned")
                records = record.recordReturn(list2,a)
            else:
                print("No record found.\nYou have not borrowed this book from this library\n")
        
    while answer == False:
        print(list3)
        a = input("Press y to borrow/return more books and n to exit").lower()
        if a == "y" or a =="n":
            answer = True
        else:
            answer = False

total1 = bill.billborrow(list1,list3)
total2 = bill.billreturn(list2,list4)
print("you need to pay",total1+total2)
