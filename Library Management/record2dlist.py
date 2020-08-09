def record2dlist(list2):
	record = open("record.txt","r")
	for i in record:
		list2.append(i.split(","))
