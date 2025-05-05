def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
num = int(input("Enter a number to find factorial: "))
print(f"Factorial of {num} is {factorial(num)}")

def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
values = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Largest number is:", find_largest(values))

import math
def area_circle(radius):
    return math.pi * radius ** 2
def area_rectangle(length, width):
    return length * width
def area_square(side):
    return side ** 2
print("Choose shape: 1. Circle 2. Rectangle 3. Square")
choice = int(input("Enter your choice (1/2/3): "))
if choice == 1:
    r = float(input("Enter radius: "))
    print("Area of circle:", area_circle(r))
elif choice == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area of rectangle:", area_rectangle(l, w))
elif choice == 3:
    s = float(input("Enter side: "))
    print("Area of square:", area_square(s))
else:
    print("Invalid choice.")

