# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

counter = 0
odd = []
while counter < 10:
    nums = float(input("Enter 10 numbers: "))
    counter += 1

    if nums % 2 != 0:
        odd.append(nums)

print(len(odd))