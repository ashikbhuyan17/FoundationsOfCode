<img src='./images/programming.jpg' alt='FoundationsOfCode' id='header'/>

<h1 align="center" >Foundations Of Code</h1>


<div align="center" >

<a href="mailto:jibon.py.@gmail.com">
<img
src='https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white'
alt='Jibon Ahmed'
/>
</a>

<a href="tel:+8801987132107">
<img
src='https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white'
alt='Jibon Ahmed'
/>
</a>
<a href="#" target="_blank">
<img
src='https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white'
alt='Jibon Ahmed'
/>
</a>
<a href="https://www.facebook.com/jibon969" target="_blank">
<img
src='https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white'
alt='Jibon Ahmed'
/>
</a>

<a href="https://www.linkedin.com/in/jibon969/" target="_blank">
<img
src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white'
alt='Jibon Ahmed'
/>
</a>

<a href="https://github.com/jibon969" target="_blank">
<img
src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white'
alt='Jibon Ahmed'
/>
</a>

</div>


#### 01. Hello World 
```
Output : Hello World
```
<details><summary style="cursor:pointer">Solution</summary>

```py
print("Hello World")
```
</details>

#### 02. Print Own Name
```
Output : Jibon Ahmed
```

<details><summary style="cursor:pointer">Solution</summary>

```py
print("Jibon Ahmed")
```
</details>

#### 03. Print an Integer Entered By the User
```
Input  : 6
Output : 6
```
<details><summary style="cursor:pointer">Solution</summary>

```py
number = int(input("Please Enter your number : "))
print(number)
```
</details>


#### 04. Add Two Numbers

```
Input: num1 = 5, num2 = 10
Output: 15
Explanation: 342 + 465 = 807

Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```

<details><summary style="cursor:pointer">Solution</summary>

```py
num1 = 5;
num2 = 10;
sum = num1 + num2;
print(sum); // Output: 15
```
</details>

#### 05. Check prime number or not
```
Input: num1 = 7
Output: prime number
```
<details><summary style="cursor:pointer">Solution</summary>

```py
number = 7
if number % 2 == 0:
    print("Not, A prime number ", number)
else:
    print("it's prime number ", number)
```
</details>

#### 06. Multiply two Floating-Point Numbers 
```
Input: 
num1 = 10.4
num2 = 20.4
Output: 30.799999999999997
```

<details><summary style="cursor:pointer">Solution</summary>

```py
num1 = 10.4
num2 = 20.4
multiply = num1 * num2
print(multiply)
```
</details>

#### 07. ASCII Character
```
Input  : 'A'
output : 65
```
<details><summary style="cursor:pointer">Solution</summary>

```py
value = 'A'
print(ord(value))
```
</details>

#### 08. Swap Two Number
```
Input   : a = 5
        : b = 6
Output  : a = 6
        : b = 5
```

<details><summary style="cursor:pointer">Solution</summary>

```py
a = 5
b = 6
a, b = b, a
print(a)
print(b)
```
</details>

#### 09. Calculate Fahrenheit to Celsius

```
Input   : Fahrenheit= 50
Output  : 10.0
Formula : Fahrenheit-32)*5)/9
```
<details><summary style="cursor:pointer">Solution</summary>

```py
Fahrenheit= 54.
Celsius = ((Fahrenheit-32)*5)/9.
print("Temperature in Celsius is: ", Celsius);
```
</details>


#### 10.  Find the Size of int, float, double, and char

```
The getsizeof() function returns the number of bytes that Python uses to represent an integer.
```
<details><summary style="cursor:pointer">Solution</summary>

```py
from sys import getsizeof

# integer ==============================
integer_counter = 10
integer_size = getsizeof(integer_counter)
print(f"Integer : {integer_size} ")

# Float ==============================
float_counter = 10.4
float_size = getsizeof(float_counter)
print(f"Float : {float_size}")

# Char ===========================
char_counter = 'A'
char_size = getsizeof(char_counter)
print(f"Char : {char_size}")
```
</details>

#### 11. Add Two Complex Numbers 

```
Input : 
        num1 = 3 + 6j
        num2 = 4 + 2j
Output : (7+8j)
```
<details><summary style="cursor:pointer">Solution</summary>

```py
num1 = 3 + 6j
num2 = 4 + 2j
sum = num1 + num2
print(sum)
```
</details>

#### 12. Prime Numbers From 1 to N 

```
Input : 5
Output : 
1 is a Prime Number
2 is Not a Prime Number
3 is a Prime Number
4 is Not a Prime Number
5 is a Prime Number
```
<details><summary style="cursor:pointer">Solution</summary>

```py
n = int(input("Enter your number : "))
number = 1
while number <= n:
    if number % 2 == 0:
        print(f"{number} is Not a Prime Number")
    else:
         print(f"{number} is a Prime Number")
    number += 1
```
</details>

#### 13. Find Simple Interest

```
Input: Principal (amount): 1200 
Rate: 5.3
Time: 2
Output : 126.0
```
<details><summary style="cursor:pointer">Solution</summary>

```py
simple_interest = (1200*3.5*3)/100
print(simple_interest)
```
</details>


#### 14. Find Compound Interest

```
Input: 
Principal (amount): 1200 
Time: 2 
Rate: 5.4
Output : 1330.9920000000002
```
<details><summary style="cursor:pointer">Solution</summary>

```py
def compound_interest(principal, rate, time):
    # Formula = P(1 + R/100)t
    amount = principal * (pow((1 + rate / 100), time))
    ci = amount - principal
    print("Compound interest is : ", ci)
compound_interest(12000, 5.4, 2)
```
</details>


#### 15. Area And Perimeter Of Rectangle 

```
Input :
length = 10 
breadth = 10 
Output : 
area      = 100 
perimeter = 40 
```
<details><summary style="cursor:pointer">Solution</summary>

```py
length = 10 
breadth = 10 
area = 2*(length+breadth)
print(area)

perimeter = length * breadth
print(perimeter)
```
</details>

---
**[⬆ Back to Top](#header)**





