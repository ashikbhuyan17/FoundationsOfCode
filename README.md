<img src='./images/programming.jpg' alt='FoundationsOfCode' id='header'/>

<h1 align="center" >Foundations Of Code</h1>


<div align="center" >

<a href="mailto:mdmithu.learner@gmail.com">
<img
src='https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white'
alt='Mithu'
/>
</a>

<a href="tel:+8801324203138">
<img
src='https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white'
alt='Mithu'
/>
</a>
<a href="#" target="_blank">
<img
src='https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white'
alt='Mithu'
/>
</a>
<a href="https://www.facebook.com/" target="_blank">
<img
src='https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white'
alt='Mithu'
/>
</a>

<a href="https://www.linkedin.com/in/mithucloud007/" target="_blank">
<img
src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white'
alt='Mithu'
/>
</a>

<a href="https://github.com/MithuCloud007" target="_blank">
<img
src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white'
alt='Mithu'
/>
</a>

</div>

<!-- <h1 align="center" >Array CRUD(create,read,update,delete) Operation </h1> -->


#### 01. Add Two Numbers

```
Input: num1 = 5, num2 = 10
Output: 15
Explanation: 342 + 465 = 807

Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```

<details><summary style="cursor:pointer">Solution</summary>

```python
num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

add = num1 + num2
print(add)
```  

</details>

#### 02. Swap two Numbers

```
Input: number1 = 10, number2 = 20
Output: number1 = 20, number2 = 10

Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```

<details><summary style="cursor:pointer">Solution</summary>

```python
number1 = 10
number2 = 20

number1, number2 = number2, number1
print(number1)
print(number2)


```  


</details>

#### 03. Check Prime Number 

```
Input: number = 10
Output: It Is Prime Number

Complexity Analysis
    Time Complexity: O(n)
    Auxiliary Space: O(1)
```

<details><summary style="cursor:pointer">Solution</summary>

```python
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


```  


</details>

#### 04. Calculate Fahrenheit to Celsius

```
Input: Fahrenfeit = 40.0
Output: Celsius = Temperature in Celsius is: 4.44

Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```

<details><summary style="cursor:pointer">Solution</summary>


```python

Fahrenheit= 40.0
Celsius = ((Fahrenheit-32.0)*5)/9.0
print(f"Temperature in Celsius is: {Celsius:.2f}")


```  

---
**[⬆ Back to Top](#header)**


</details>



