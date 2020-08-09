import datetime
def billborrow(list1,list3):
    total = 0
    for i in list3:
        total += float(list1[i][-1])
    return total
        
def billreturn(list2,list4):
    total = 0
    for i in list4:
        string_date = list2[i][3]
        format = "%Y-%m-%d"
        datetime_object = datetime.datetime.strptime(string_date, format)
        print(datetime_object)
        time =datetime.datetime.today()-datetime_object
        if time.days >= 10:
            total += (total.days - 9) * 0.1
    return total
