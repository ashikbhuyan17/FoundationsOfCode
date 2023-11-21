
# Find the Size of int, float, double, and char
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