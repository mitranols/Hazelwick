second = int(input("Enter a number of seconds: "))
print(f"{second} seconds is {second // 3600} hour(s), {(second % 3600) // 60} minute(s) and {(second % 3600) % 60} second(s)")