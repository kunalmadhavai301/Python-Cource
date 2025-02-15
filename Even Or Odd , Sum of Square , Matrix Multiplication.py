#Matrix Multipliation 
print("Enter the first 2x2 matrix:")
a11 = int(input("Enter element (1,1): "))
a12 = int(input("Enter element (1,2): "))
a21 = int(input("Enter element (2,1): "))
a22 = int(input("Enter element (2,2): "))
print("Enter the second 2x2 matrix:")
b11 = int(input("Enter element (1,1): "))
b12 = int(input("Enter element (1,2): "))
b21 = int(input("Enter element (2,1): "))
b22 = int(input("Enter element (2,2): "))
print("\nMatrix Addition:")
print(f"[{a11 + b11} {a12 + b12}]")
print(f"[{a21 + b21} {a22 + b22}]")
print("\nMatrix Subtraction:")
print(f"[{a11 - b11} {a12 - b12}]")
print(f"[{a21 - b21} {a22 - b22}]")
print("\nMatrix Multiplication:")
m11 = a11 * b11 + a12 * b21
m12 = a11 * b12 + a12 * b22
m21 = a21 * b11 + a22 * b21
m22 = a21 * b12 + a22 * b22
print(f"[{m11} {m12}]")
print(f"[{m21} {m22}]")

#Even Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is not even.")

#Sum of Square
sum = 0
for i in range(21, 31):
    sum += i ** 2
print(f"The sum of squares of numbers from 21 to 30 is: {sum}")
