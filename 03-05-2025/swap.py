print("1. Swap two variables")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
a, b = b, a  
print(f"After swapping: a = {a}, b = {b}\n")
print("2. Circulate values of three variables")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
a, b, c = c, a, b
print(f"After circulation: a = {a}, b = {b}, c = {c}\n")
print("3. Distance between two points")
x1 = float(input("Enter x-coordinate of first point: "))
y1 = float(input("Enter y-coordinate of first point: "))
x2 = float(input("Enter x-coordinate of second point: "))
y2 = float(input("Enter y-coordinate of second point: "))
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print(f"Distance between the two points is: {distance}")
