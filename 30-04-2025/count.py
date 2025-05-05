string = input("Enter a string: ")
char_to_count = input("Enter a character to count: ")
count = 0
for char in string:
    if char == char_to_count:
        count += 1
print("The character", char_to_count, "appears", count, "time(s) in the string.")
