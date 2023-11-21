# Python Program to Print Prime Numbers From 1 to N 

n = int(input("Enter your number : "))
number = 1
while number <= n:
    if number % 2 == 0:
        print(f"{number} is Not a Prime Number")
    else:
         print(f"{number} is a Prime Number")
    number += 1

