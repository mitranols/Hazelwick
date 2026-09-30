print("---Shopping List---")
print("1. Add an item")
print("2. Remove an item")
print("3. View the list")
print("4. Count items")
print("5. Quit")
error = 0
list = []
sel = int(input("Choose an option: "))
while sel != 5:
    if sel == 1:
        item = input("Item to add: ")
        for i in range(len(list)):
            if list[i] == item:
                print(f"{item} is already on the list.")
                error += 1
                break
        if error == 0:
            list.append(item)