print("---Shopping List---")
print("1. Add an item")
print("2. Remove an item")
print("3. View the list")
print("4. Count items")
print("5. Quit")
shops = []
sel = int(input("Choose an option: "))
while sel != 5:
    # add an item
    if sel == 1:
        item = input("Item to add: ")
        # check for dupes
        if item in shops:
             print(f"{item} is already in the list")
        # addition of item
        else:
             shops.append(item)
             print(f"{item} has been added to the list.")
    # remove an item
    elif sel == 2:
        item = input("Item to remove: ")
        if item in shops:
            shops.remove(item)
            print(f"{item} removed.")
        else:
            print(f"{item} is not in the list")
    elif sel == 3:
        for i in range(len(shops)):
            print (f"{i+1}. {shops[i-1]}")
    elif sel == 4:
        print(f"The amount of items in the list is: {len(shops)}")
    else:
        print(f"{sel} is not an option. Pick a number 1-5")
    sel = int(input("Choose an option: "))
print("Goodbye!")