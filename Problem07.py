# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

numbers = input("Input 10 numbers (Use , and a space after to separate): ").split(", ")    # split: divides the number string excluding ", "
Lnum = []                                                                # list initialization
add = 0

for num in numbers:                                    # Line 7-8: puts the divided strings in numbers into the Lnum list
    Lnum.append(float(num))                              # Lnum.append(int(num)) also makes the string into integers 

for x in range(0, len(Lnum)):                          # for adding the numbers inside Lnum list 
    add += Lnum[x]                                     # Lnum[x] = kinukuha ung value ng may index na x sa Lnum

print(add)