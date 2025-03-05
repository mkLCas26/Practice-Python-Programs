# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

numbers = input("Enter 10 numbers (Use , and a space after to separate): ").split(", ")
Num = []
Odd = []


for val in numbers:
    Num.append(float(val))

for num in Num:
    if num % 2 != 0:
        Odd.append(num)

print(Odd)