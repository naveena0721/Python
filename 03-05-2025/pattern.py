n = int(input("Enter a number for even number series: "))
print("Even number series up to", n, ":")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=' ')
print("\n")

rows = int(input("Enter number of rows for number pattern: "))
print("Number Pattern:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

height = int(input("Enter height for star pyramid: "))
print("Star Pyramid Pattern:")
for i in range(1, height + 1):
    # Print spaces
    for j in range(height - i):
        print(" ", end='')
    # Print stars
    for k in range(2 * i - 1):
        print("*", end='')
    print()


