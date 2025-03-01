# Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)

even = []

for x in range(0, 101):
    if x % 2 == 0:
        even.append(x)

print(even)

