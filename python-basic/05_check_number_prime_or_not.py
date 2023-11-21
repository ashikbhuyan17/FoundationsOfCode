# Program to Check Whether a Number is Prime or Not

num=int(input('Enter a Number: '))
count=0
for i in range(2,num):
    if (num%i==0):
        count+=1
    break
if (count==0):
    print("It Is Prime Number")
else:
    print("It is NOT prime number")  