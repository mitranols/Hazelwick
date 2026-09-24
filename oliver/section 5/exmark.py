exmark = int(input("Enter a mark (or -1 to finish): "))
totmark = 0
if exmark < 0 or exmark > 100:
    print("Invalid mark - must be 0 to 100.")
if exmark >= 0 and exmark <= 100:
    lowmark = exmark
    highmark = exmark
average = 0
while exmark != -1:
    if exmark < 0 or exmark > 100:
        print("Invalid mark - must be 0 to 100.")
        exmark = int(input("Enter a mark (or -1 to finish): "))
    elif exmark >= 0 and exmark <= 100:
        totmark += 1
        average = average + exmark
        if exmark < lowmark:
            lowmark = exmark
        elif exmark > highmark:
            highmark = exmark
        exmark = int(input("Enter a mark (or -1 to finish): "))
print(f"Marks entered: {totmark}")
print(f"Average: {average / totmark}")
print(f"Highest: {highmark}")
print(f"Lowest: {lowmark}")

