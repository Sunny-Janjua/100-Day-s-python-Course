# You must install this first: pip install sympy
from sympy import isprime

number = int(input("Enter your number: "))

if isprime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")