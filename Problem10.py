# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

noZero = []

for num in range(0, 100):
    if num % 10 != 0:                       # excludes 0 kase kapag yun na yung iteration magiging 0 != 0 siya 
        noZero.append(num)

print(noZero)

