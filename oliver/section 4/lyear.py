year = int(input("Enter the year"))
isleap = 0
# leap year solve
if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
            isleap = 1
        else:
            print("Not leap year")
    else:
        print("Leap year")
        isleap = 1
else:
    print("Not Leap year")
# month days
month = int(input("Enter a month number (1-12): "))
days = 0
if month == 2 and isleap == 1:
    days = 29
elif month == 2 and isleap != 0:
    days = 28
elif month == 4 or 6 or 9 or 11:
    days = 30
else:
    days = 31
print (f"Month {month} of {year} has {days} days.")