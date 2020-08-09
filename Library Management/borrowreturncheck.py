def recordborrow(list1,list2,name,snumber):
    for i in list2:
        if name in i and list1[int(snumber)][1] in i and i[2]=="YES" and i[4]=="NO":
            print("CANNOT BORROW\nYOU HAVE NOT RETURNED THE PREVIOUS BOOK\n")
            return False
    return True
        
def recordreturn(list1,list2,name,snumber,list4):
    a = 0
    for i in list2:
        a += 1
        if name in i and list1[int(snumber)][1] in i and i[2]=="YES" and i[4]=="NO":
            list4.append(a-1)
            return True,a-1
    return False,None
        
        
