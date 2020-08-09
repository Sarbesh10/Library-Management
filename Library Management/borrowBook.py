def borrowBook(list1,snumber):
    list1[int(snumber)][3] = str(int(list1[int(snumber)][3])-1)
    file = open("librarybook.txt","w")
    for i in list1:
        i = ','.join(i)
        file.write(i)
    file.close()
    

