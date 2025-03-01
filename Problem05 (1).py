# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

num1 = float(input("1st Number: "))
num2 = float(input("2nd Number: "))

while num2 == 0:
    print("Undefined")
    num1 = float(input("1st Number: "))
    num2 = float(input("2nd Number: "))

    if num2 != 0:
            quo = num1 / num2
            print(quo) 
