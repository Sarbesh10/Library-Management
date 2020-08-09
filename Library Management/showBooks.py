def showBooks(list1):

    for i in range(len(list1)):
        for j in range(len(list1[i])):
            if j == 0:
                print(list1[i][j],end="   ")
            elif len(list1[i][j])>18:
                print(list1[i][j],end="\t")
            elif len(list1[i][j])>13:
                print(list1[i][j],end="\t\t")
            else:
                print(list1[i][j],end="\t\t\t")
        print("\n")
            
