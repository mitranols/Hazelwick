exmark = int(input("Enter a mark (or -1 to finish): "))
totmark = 0
lowmark = -1
highmark = -1
star = ""
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
        for i in range(exmark//10):
            star += "*"
        print(star)
        star = ""
        exmark = int(input("Enter a mark (or -1 to finish): "))
print(f"Marks entered: {totmark}")
if average == 0:
    print("Average: 0 (You should've entered valid marks)")
elif average > 0:
    print(f"Average: {average / totmark}")
if highmark >= 0 and highmark <= 100 and lowmark >= 0 and lowmark <= 100:
    print(f"Highest: {highmark}")
    print(f"Lowest: {lowmark}")
else:
    print("No valid marks entered to calculate highest and lowest marks.")

