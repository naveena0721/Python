num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
a, b = num1, num2
while b != 0:
    a, b = b, a % b
gcd = a
lcm = (num1 * num2) // gcd
print(f"GCD of {num1} and {num2} is: {gcd}")
print(f"LCM of {num1} and {num2} is: {lcm}")
