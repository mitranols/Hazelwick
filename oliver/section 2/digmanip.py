num = int(input("Enter a 3-digit number: "))
print(f"Hundreds: {num // 100}")
print(f"Tens: {(num % 100) // 10}")
print(f"Units: {(num % 100) % 10}")
sum = ((num // 100)) + ((num % 100) // 10) + ((num % 100) % 10)
print(f"Sum of digits: {sum}")
if str(num)[2] != "0" :
    print(f"Reversed: {((num % 100) % 10)}{((num % 100) // 10)}{num // 100}")
if str(num)[2] == "0" :
    print(f"Reversed: {((num % 100) // 10)}{num // 100}")
print(f"Even number: {(num % 2) == 0}")