print("---Shopping List---")
print("1. Add an item")
print("2. Remove an item")
print("3. View the list")
print("4. Count items")
print("5. Quit")
lists = []
sel = int(input("Choose an option: "))
while sel != 5:
    # add an item
    if sel == 1:
        item = input("Item to add: ")
        # check for dupes
        if item in lists == True:
             print("Item already in list")
        # addition of item
        elif item in lists != True:
             lists.append(item)
    # remove an item
    elif sel == 2:
        item = input("Item to remove: ")
        if item in lists == True:
            lists.remove(item)
        elif item in lists != False:
            print("Item not in list")
    elif sel == 3:
        for i in range(len(lists)):
            print (f"{i}. {lists[i-1]}")
            print()
    sel = int(input("Choose an option: "))