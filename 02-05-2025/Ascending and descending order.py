n = int(input("Enter the number n: "))
print("Numbers in ascending order:")
for i in range(1, n + 1):
    print(i, end=' ')
print("\n")
print("Numbers in descending order:")
for i in range(n, 0, -1):
    print(i, end=' ')
