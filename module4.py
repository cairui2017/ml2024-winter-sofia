# module4.py

N = int(input("Enter the value of N (positive integer): "))
numbers = []

for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

X = int(input("Enter the value of X (integer): "))

if X in numbers:
    index = numbers.index(X) + 1
    print(f"The index of {X} is: {index}")
else:
    print("-1")
