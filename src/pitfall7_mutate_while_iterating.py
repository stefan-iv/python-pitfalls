mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for item in mylist:
    if item % 2 == 0:
        mylist.remove(item)

print(mylist)
