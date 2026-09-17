name = input("What is your name? ")
height = float(input("Enter your height in cm: "))
metre = height / 100
INCH = 2.54
print(f"Hi {name.title()}!")
print(f"Your height is {height} m.")
print(f"That is {round((height / 2.54), 2)} inches.")
print(f"Taller than 180 cm: {height>180}")