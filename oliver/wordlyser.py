word = input("Enter a word: ")
lower = word.lower()
middle = word[(len(word)) // 2)]
print(f"Reversed: {word[::-1]}")
print(f"Uppercase: {word.upper()}")
print(f"Length: {len(word)}")
print(f"Palindrome: {lower == lower[::-1]}")
print(f"First letter character code: {ord(word[0])}")
print(f"Middle character: {middle}")