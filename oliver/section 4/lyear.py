year = int(input("Enter the year: "))
isleap = 0
# leap year solve
if year % 4 == 0 or (year % 4 == 0 and year % 100 == 0 and year % 400):
    print(f"Year {year} is a leap year.")
    isleap = 1
else:
    print(f"Year {year} is not a leap year.")
# month days
month = int(input("Enter a month number (1-12): "))
days = 0
if month == 2 and isleap == 1:
    days = 29
elif month == 2 and isleap != 1:
    days = 28
elif month == (4 or 6 or 9 or 11):
    days = 30
else:
    days = 31
print (f"Month {month} of {year} has {days} days.")