# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

count = 0
sum = 0

while count < 10:
    count += 1
    number = float(input("Enter 10 numbers: "))

    sum += number

print (sum)
