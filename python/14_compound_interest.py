# Python Program to Find Compound Interest
""" 
Amount= P(1 + R/100)t
Compound Interest = Amount – P
Where, 
P is principal amount 
R is the rate and 
T is the time span
"""

""" 
Input: Principal (amount): 1200 Time: 2 Rate: 5.4
Output : 1330.9920000000002
"""

def compound_interest(principal, rate, time):
 
    # Formula = P(1 + R/100)t
    amount = principal * (pow((1 + rate / 100), time))
    ci = amount - principal
    print("Compound interest is : ", ci)
 
compound_interest(12000, 5.4, 2)