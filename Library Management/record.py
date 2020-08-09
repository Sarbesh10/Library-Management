import datetime
def record(name,list1,types,snumber):
    fh = open("record.txt", "a")
    fh.write(name)
    fh.write(",")
    fh.write(list1[int(snumber)][1])#book_name
    fh.write(",")
    fh.write("YES")#borrow_book
    fh.write(",")
    fh.write(str(datetime.date.today()))#borrowed_time
    fh.write(",")
    fh.write("NO")#reutrn_book
    fh.write(",")
    fh.write("NO")#return_time
    fh.write(",")
    fh.write(str(list1[int(snumber)][4]))#price
    fh.write("\n")
    
    fh.close()
    
def recordReturn(list2,a):
    record = open("record.txt","w")
    list2[a][4] = "YES"
    list2[a][5] = str(datetime.date.today())
    for i in list2:
        i = ','.join(i)
        record.write(i)
    record.close()
    
