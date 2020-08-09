def list2d(list1):
    library = open("librarybook.txt","r")
    for i in library:
        list1.append(i.split(","))
    library.close()
    return 



