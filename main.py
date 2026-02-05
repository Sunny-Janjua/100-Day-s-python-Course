# ## 🐍 Python – 300 Practice Program Questions (Beginner → Advanced)
# ## 🟢 LEVEL 1: Python Basics (1–50)

# # 1. Print "Hello, World"
# print("Hello, World")
# # 2. Print your name
# print("Code With Sunny Janjua")
# # 3. Print a number
# print(443344434433)
# # 4. Take input from user and print it
# name=input("Enter Your name : ")
# rollNo=input("Enter your roll No : ")
# rollNo=int(rollNo)
# print(type(rollNo))
# print(f"my name is {name} and roll No is {rollNo}")
# # 5. Add two numbers
# num1=input("Enter your First number : ")
# num2=input("Enter your Second number : ")
# num1=int(num1)
# num2=int(num2)
# print(type(num1))
# print(type(num2))
# sum=num1+num2
# print(f"The Sum of num1 {num1} and num2 {num2} is : ",sum)
# # 6. Subtract two numbers
# num1=int(input("Enter your First number : "))
# num2=int(input("Enter your Second number : "))
# print(num1-num2)
# # 7. Multiply two numbers
# num1=int(input("Enter your First number : "))
# num2=int(input("Enter your Second number : "))
# print(num1*num2)
# # 8. Divide two numbers
# num1=int(input("Enter your First number : "))
# num2=int(input("Enter your Second number : "))
# print(num1/num2)
# # 9. Find remainder of two numbers
# num1=int(input("Enter your First number : "))
# num2=int(input("Enter your Second number : "))
# print(num1%num2)
# # 10. Find power of a number
# num1=int(input("Enter your First number : "))
# num2=int(input("Enter your Second number : "))
# print(num1**num2)
# # 11. Swap two variables
# num1=10
# num2=20
# print(num1)
# print(num2)
# temp=num1
# num1=num2
# num2=temp
# print(num1)
# print(num2)

# num1=10
# num2=20

# print("number one : ", num1)
# print("number two : ", num2)

# num1=num1+num2
# num2=num1-num2
# num1=num1-num2

# print("number one : ", num1)
# print("number two : ", num2)

# a = 5
# b = 10

# print(a)
# print(b)

# a = a * b
# b = a / b
# a = a / b

# print(a, b)

# a = 5
# b = 10

# print(a)
# print(b)

# a, b = b, a
# print(a, b)  # 10 5


# # 12. Convert Celsius to Fahrenheit
# def temp(temprature):
#     c = 5/9*(temprature-32)
#     return f"the temprature fo my is {c}"
# result=temp(3434)
# print(f"The Result of Celsius to Fahrenheit {result}")
# # 13. Convert Fahrenheit to Celsius
# def temp(temprature):
#     c =(9/5)*temprature+32
#     return f"the temprature fo my is {c}"
# result=temp(3434)
# print(f"The Result of Fehrenheit to Celsius {result}")

# 14. Calculate simple 
# P = Principal amount
# R = Rate of interest (per year)
# T = Time (in years)

# def simple_interest(p, r, t):
#     return (p * r * t) / 100

# print(simple_interest(10000, 5, 2))

# principal_amount=int(input("Enter your principal amount : "))
# Rate_of_interes=int(input("Enter your Rate of interes : "))
# Time=int(input("Enter your Time : "))

# def interest(principal_amount,Rate_of_interes,Time):
#     result=(principal_amount*Rate_of_interes*Time)/100
#     return result

# my_interest=interest(principal_amount,Rate_of_interes,Time)
# print(f"My total interest is {my_interest}")

# # 15. Calculate area of rectangle
# height=int(input("Enter your height : "))
# width=int(input("Enter your width : "))

# def area(height,width):
#     erea=height*width
#     return erea

# my_erea=area(height,width)
# print(f"The result of my rectangular is : {my_erea}")

# import math

# radius = float(input("Enter your radius: "))

# def area_of_circle(r):
#     area = math.pi * r * r
#     return area

# print(area_of_circle(radius))

# # 17. Check even or odd number

# my_number=int(input("Enter your number : "))

# def check_number(my_number):
#     if my_number%2==0:
#         return f"Even Number {my_number}"
#     else:
#         return f"Odd Number {my_number}"

# print(check_number(my_number))

# # 18. Check positive or negative
# my_number=int(input("Enter your number : "))

# def check_number(my_number):
#     if my_number<0:
#         return f"Negative Number {my_number}"
#     else:
#         return f"Positive Number {my_number}"

# print(check_number(my_number))

# 19. Find largest of two numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a > b:
#     print(f"{a} is the largest number")
# else:
#     print(f"{b} is the largest number")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# largest = max(a, b)
# print(f"{largest} is the largest number")

# def largest_of_two(a, b):
#     return a if a > b else b

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print(f"{largest_of_two(a, b)} is the largest number")

# # 20. Find smallest of two numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a < b:
#     print(f"{a} is the smallest number")
# else:
#     print(f"{b} is the largest number")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# largest = min(a, b)
# print(f"{largest} is the smallest number")

# def largest_of_two(a, b):
#     return a if a < b else b

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print(f"{largest_of_two(a, b)} is the smallest number")

# 21. Check leap year
# year=int(input("Enter your Leap year : "))

# if year%2==0 and year%4==0:
#     print("Leap Year")
# else:
#     print("Not Leap Year")
# # 22. Print numbers from 1 to 10
# number=1
# while(number<=10):
#     print(number)
#     number+=1

# for i in range(11):
#     print(f"The number is : {i}")
# # 23. Print numbers from 10 to 1
# number=10
# while(number>=1):
#     print(number)
#     number-=1

# for i in range(10,0,-1):
#     print(f"The number is : {i}")

# 24. Print even numbers till N
# number=int(input("Enter your number : "))
# for i in range(0,number,2):
#     # if i%2==0:
#     print(f"the even number is {i}")
# # 25. Print odd numbers till N
# number=int(input("Enter your number : "))
# for i in range(1,number,2):
#     # if i%2==0:
#     print(f"the odd number is {i}")

# 26. Find sum of first N numbers
# number = int(input("Enter your number: "))
# mysum = 0

# for i in range(1, number + 1):
#     mysum=mysum+i

# print(mysum)
# # 27. Find factorial of a number

# number=int(input("Enter your factorail number : "))
# def factorail(number):
#     fact=1
#     for i in range(1,number+1):
#         fact=fact*i
#     return fact
# my_fact=factorail(number)
# print(my_fact)
# # 28. Find square of a number

# number=int(input("Enter your square number : "))
# def square_of_number(number):
#     return number**2

# print(square_of_number(number))


# # 29. Find cube of a number

# number=int(input("Enter your Cube number : "))
# def square_of_number(number):
#     return number**3

# print(square_of_number(number))
# 30. Find ASCII value of character

# char = 'A'
# ascii_code = ord(char)
# print(ascii_code)

# print(ord('a'))   # 97
# print(ord('Z'))   # 90
# print(ord('0'))   # 48
# print(ord('@'))   # 64


# print(chr(65))   # A
# print(chr(97))   # a




# # 31. Convert string to integer
# number="123"
# print(type(number))
# number=int(number)
# print(type(number))



# # 32. Convert integer to string

# number=54443
# print(type(number))

# number=str(number)
# print(type(number))

# # 33. Print length of string

# name="hello sunny code studio"
# print(type(name))
# print(name)
# print(len(name))

# # 34. Reverse a string
# name="sunnyjanjua"
# print(name)
# newName=name[::-1]
# print(newName)

# text = "Python"
# reversed_text = "".join(reversed(text))
# print(reversed_text)


# 35. Check palindrome string

# myName="madam"
# print(f"name first changing {myName}")
# print(myName)

# name=myName[::-1]
# print(f"name changing {name}")

# name=input("Enter your name : ")

# name=name[::-1]
# print(name)
# if name==name[0:len(name)+1:-1]:
#     print("Well come to Palindrom")
# else:
#     print("not")

# def is_palindrome(text):
#     return text == text[::-1]

# print(is_palindrome("level"))   # True
# print(is_palindrome("hello"))   # False

# name=input("Enter your name")
# newname=name[::-1]
# print(f"name changing {newname}")


# text = "radar"
# reverse = ""

# for char in text:
#     reverse = char + reverse

# if text == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# text = "A man a plan a canal Panama"

# clean_text = text.replace(" ", "").lower()

# if clean_text == clean_text[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# 36. Count vowels in string

# string="sunny janjua"
# count=0
# for i in string:
#     if i in "aeiou":
#         count+=1

# print(count)

# def count_vowels(s):
#     vowels = "aeiou"
#     count = 0
#     for char in s.lower():
#         if char in vowels:
#             count += 1
#     return count

# print(count_vowels("programming make life easy"))

# string = "sunny janjua"
# print(sum(1 for i in string if i in "aeiou"))

# 37. Count consonants in string

# check=input("Enter your consonants : ")

# vowels="aeiou"

# if check in vowels:
#     print("Not consonants")
# else:
#     print("consonants")

# string = input("Enter a string: ")

# vowels = "aeiouAEIOU"
# count = 0

# for ch in string:
#     if ch.isalpha() and ch not in vowels:
#         count += 1

# print("Total consonants:", count)

# ch = input("Enter a character: ")

# vowels = "aeiouAEIOU"

# if ch.isalpha():
#     if ch in vowels:
#         print("Not a consonant")
#     else:
#         print("Consonant")
# else:
#     print("Not an alphabet")




# 38. Count digits in number

# number = int(input("Enter a number: "))

# count = 0

# while number != 0:
#     count += 1
#     number //= 10

# print("Total digits:", count)

# number = input("Enter a number: ")
# print(len(number))


# number = int(input("Enter a number: "))

# if number == 0:
#     print("Total digits: 1")
# else:
#     count = 0
#     while number != 0:
#         count += 1
#         number //= 10
#     print("Total digits:", count)


# def encode(text, shift):
#     result = ""
#     for ch in text:
#         if ch.isalpha():
#             if ch.islower():
#                 result += chr((ord(ch) - 97 + shift) % 26 + 97)
#             else:
#                 result += chr((ord(ch) - 65 + shift) % 26 + 65)
#         else:
#             result += ch
#     return result


# def decode(text, shift):
#     result = ""
#     for ch in text:
#         if ch.isalpha():
#             if ch.islower():
#                 result += chr((ord(ch) - 97 - shift) % 26 + 97)
#             else:
#                 result += chr((ord(ch) - 65 - shift) % 26 + 65)
#         else:
#             result += ch
#     return result


# # ---- USER INPUT ----
# message = input("Enter your message: ")
# shift = int(input("Enter secret key (number): "))

# encoded = encode(message, shift)
# decoded = decode(encoded, shift)

# print("\nEncoded message:", encoded)
# print("Decoded message:", decoded)


# 39. Find largest of three numbers

# number1=int(input("Enter first number : "))
# number2=int(input("Enter second number : "))
# number3=int(input("Enter third number : "))

# if number1>number2:
#     print(f"Number one is a largest number in three number { number1}")

# elif number2>number3:
#     print(f"Number one is a largest number in three number { number2}")

# else:
#     print(f"Number one is a largest number in three number { number3}")


# # 39. Find largest of three numbers

# number1 = int(input("Enter first number : "))
# number2 = int(input("Enter second number : "))
# number3 = int(input("Enter third number : "))

# # Check if number1 is greater than BOTH number2 AND number3
# if number1 >= number2 and number1 >= number3:
#     print(f"The largest number is: {number1}")

# # Check if number2 is greater than BOTH number1 AND number3
# elif number2 >= number1 and number2 >= number3:
#     print(f"The largest number is: {number2}")

# # If neither of the above is true, number3 must be the largest
# else:
#     print(f"The largest number is: {number3}")

# number1 = int(input("Enter first number : "))
# number2 = int(input("Enter second number : "))
# number3 = int(input("Enter third number : "))

# largest = max(number1, number2, number3)

# print(f"The largest number is: {largest}")




# 40. Check number is prime

# 40. Check number is prime

# number = int(input("Enter your number: "))

# # --- PART 1: Check if Even or Odd ---
# # We check this once, outside of any loop.
# if number % 2 == 0:
#     print(f"{number} is an Even number.")
# else:
#     print(f"{number} is an Odd number.")

# # --- PART 2: Check if Prime ---
# if number > 1:
#     # Check for factors from 2 up to the number itself
#     for i in range(2, number):
#         if (number % i) == 0:
#             print(f"{number} is NOT a prime number (it is divisible by {i}).")
#             break 
#     else:
#         # This runs if the loop finished without finding any factors
#         print(f"{number} is a PRIME number.")

# else:
#     # Numbers less than or equal to 1 are not prime
#     print(f"{number} is NOT a prime number.")

# # You must install this first: pip install sympy
# from sympy import isprime

# number = int(input("Enter your number: "))

# if isprime(number):
#     print(f"{number} is a prime number")
# else:
#     print(f"{number} is not a prime number")

# 41. Print all primes till N

# from sympy import isprime  # Mistake 1: Import was missing

# number = int(input("Enter your limit number: "))

# print(f"Primes up to {number}:")

# # Mistake 2: Range should include the number itself, so use 'number + 1'
# for i in range(number + 1):

#     if isprime(i):
#         # Mistake 3: Print 'i' (the current number), NOT 'number' (the limit)
#         print(f"{i} is a prime number")
        
#     # Mistake 4: Removed the 'else'. 
#     # Usually we don't print anything for non-primes to keep the output clean.


# 42. Check Armstrong number

# number = int(input("Enter a number: "))

# # Convert number to string to easily count digits and iterate
# num_str = str(number)
# num_digits = len(num_str)

# print(num_digits)

# sum_of_powers = 0

# for digit in num_str:
#     sum_of_powers += int(digit) ** num_digits
#     print(sum_of_powers)

# if sum_of_powers == number:


#     print(f"{number} is an Armstrong number")
# else:
#     print(f"{number} is not an Armstrong number")



# 43. Find sum of digits

# number=input("Enter you digit's : ")

# sum=0

# for i in number:
#     sum+=int(i)
# print(sum)


# # We do NOT wrap the input in int() immediately because we need it as a string to loop through it
# number = input("Enter your digits: ") 

# total = 0

# for i in number:
#     total += int(i) # Convert the character back to an integer to do math

# print("Sum of digits:", total)


# 44. Reverse a number

# my_list=[1,2,3,4,5]

# new_list=str(my_list[::-1])
# print(new_list)

# numbers=list(input("Enter your number's : "))
# print(numbers)
# newNumber=numbers[::-1]
# print(newNumber)


# number = int(input("Enter a number: "))

# # 1. Convert to string
# # 2. Slice with [::-1] to reverse
# # 3. Convert back to int
# reversed_num = int(str(number)[::-1])

# print("Reversed Number:", reversed_num)



# 45. Check palindrome number

# number = input("Enter a number: ")

# # Check if the string equals the reversed string
# if number == number[::-1]:
#     print(f"{number} is a Palindrome")
# else:
#     print(f"{number} is NOT a Palindrome")

# # 46. Print multiplication table

# number=int(input("Enter your number : "))

# for i in range(1,11):
#     print(f"{number} * {i} = {number * i}")

# 47. Find GCD of two numbers

# import math 

# my_number=math.gcd(10 ,20)
# print(my_number)

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))


# while num2 > 0:
#     # 1. Calculate remainder
#     remainder = num1 % num2
    
#     # 2. Shift values: 
#     # 'a' becomes the old 'b'
#     # 'b' becomes the remainder
#     num1=num2
#     num2 = remainder

# print(f"The GCD of {num1} and {num2} is: {num1}")

# 48. Find LCM of two numbers

# import math

# lcm=math.lcm(20,200)
# print(f"The LCM is {lcm}")

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# # 1. We need a clean copy of the inputs for the LCM formula later
# a = num1
# b = num2

# # 2. Find GCD first (using the Euclidean algorithm you just learned)
# while b > 0:
#     remainder = a % b
#     a = b
#     b = remainder

# gcd = a

# # 3. Apply the LCM Formula
# # We use // for integer division so we don't get a decimal point (e.g. 200.0)
# lcm = (num1 * num2) // gcd

# print(f"The LCM of {num1} and {num2} is: {lcm}")



# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# lcm=(num1*num2)/math.gcd(num1,num2)
# print(lcm)

# 49. Print star pattern (triangle)

# for i in range(10):
#     print(i*"*")

# # range(start, stop, step)
# for i in range(10, 0, -1):
#     print(i * "*")

# # 50. Print square star pattern

# size = 5

# for i in range(size):
#     print("*" * size)

# for i in range(5):
#     print("*"*i)

# ## 🟡 LEVEL 2: Conditions & Loops (51–100)

# 51. Menu driven calculator

# while True:
#     # 1. Display the Menu
#     print("\n--- CALCULATOR MENU ---")
#     print("1. Add (+)")
#     print("2. Subtract (-)")
#     print("3. Multiply (*)")
#     print("4. Divide (/)")
#     print("5. Exit")
    
#     # 2. Get User Choice
#     choice = input("Enter your choice (1-5): ")

#     # 3. Check for Exit FIRST
#     if choice == '5':
#         print("Exiting calculator. Goodbye!")
#         break # This stops the while loop

#     # 4. Check if choice is one of the math options
#     if choice in ('1', '2', '3', '4'):
        
#         # Get numbers from user
#         # We use float() so we can handle decimals like 5.5
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == '1':
#             print(f"Result: {num1} + {num2} = {num1 + num2}")

#         elif choice == '2':
#             print(f"Result: {num1} - {num2} = {num1 - num2}")

#         elif choice == '3':
#             print(f"Result: {num1} * {num2} = {num1 * num2}")

#         elif choice == '4':
#             # Handle Division by Zero error
#             if num2 == 0:
#                 print("Error: Cannot divide by Zero!")
#             else:
#                 print(f"Result: {num1} / {num2} = {num1 / num2}")
    
#     else:
#         # User entered something like '7' or 'apple'
#         print("Invalid input! Please enter 1, 2, 3, 4, or 5.")


# # --- SECTION 1: DEFINING FUNCTIONS ---
# # These functions don't run until we call them later.

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Error! Cannot divide by Zero."
#     else:
#         return x / y

# # --- SECTION 2: MAIN PROGRAM ---

# while True:
#     print("\n--- FUNCTION CALCULATOR ---")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")

#     choice = input("Enter choice (1/2/3/4/5): ")

#     # Check for Exit first
#     if choice == '5':
#         print("Exiting. Goodbye!")
#         break

#     # Check for valid input
#     if choice in ('1', '2', '3', '4'):
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#         except ValueError:
#             print("Invalid input! Please enter numbers only.")
#             continue # Skip the rest of the loop and start over

#         if choice == '1':
#             print(f"Result: {num1} + {num2} = {add(num1, num2)}")

#         elif choice == '2':
#             print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")

#         elif choice == '3':
#             print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")

#         elif choice == '4':
#             result = divide(num1, num2)
#             print(f"Result: {num1} / {num2} = {result}")
    
#     else:
#         print("Invalid Choice! Please select 1-5.")


# 52. Guess the number game

# import random

# while True:
#     number=int(input("Enter your number : "))
#     if number==random.random()*1:
#         print("successed")
#         break
#     else:
#         print("Try Again!")
# import random

# # 1. Generate the number OUTSIDE the loop so it doesn't change
# secret_number = random.randint(1, 100) 

# print("I have picked a number between 1 and 100.")

# while True:
#     # 2. Get the user's guess
#     try:
#         user_guess = int(input("Guess the number: "))
#     except ValueError:
#         print("Please enter a valid number!")
#         continue

#     # 3. Compare guess to secret number
#     if user_guess == secret_number:
#         print("Success! You guessed it!")
#         break  # Exit the loop
    
#     elif user_guess > secret_number:
#         print("Too high! Try again.")
        
#     else:
#         print("Too low! Try again.")

# import random

# secret_number = random.randint(1, 20) # Smaller range for quicker game
# attempts = 0

# print("\n--- GUESS THE NUMBER GAME ---")
# print("I am thinking of a number between 1 and 20.")

# while True:
#     try:
#         guess = int(input("Enter your guess: "))
#         attempts += 1 # Add 1 to score every time they guess
        
#         if guess == secret_number:
#             print(f"🎉 SUCCESS! You found the number {secret_number}!")
#             print(f"It took you {attempts} attempts.")
#             break
            
#         elif guess > secret_number:
#             print("📉 Too High!")
            
#         else:
#             print("📈 Too Low!")
            
#     except ValueError:
#         print("Invalid input. Please enter a number.")


# 53. Print Fibonacci series


# def fibonacci(number):
#     if number<=0:
#         return 1
#     # if number == 0 or number == 1:
#     #     return 1
#     else:
#         return fibonacci(number-1)+fibonacci(number-2)


# take_number=int(input("Enter your number for print Fibonacci serious : "))

# for i in range(take_number):
#     print(fibonacci(i))



# cycle=10
# a=0
# b=1
# count=0

# while count<=cycle:
#     print(a)
#     a,b=b,a+b
#     count+=1


# # 54. Print Fibonacci using loop

# cycle=10
# a=0
# b=1
# count=0

# while count<=cycle:
#     print(a)
#     a,b=b,a+b
#     count+=1
# # 55. Print Fibonacci using recursion
# def fibonacci(number):
#     if number<=0:
#         return 1
#     # if number == 0 or number == 1:
#     #     return 1
#     else:
#         return fibonacci(number-1)+fibonacci(number-2)


# take_number=int(input("Enter your number for print Fibonacci serious : "))

# for i in range(take_number):
#     print(fibonacci(i))


# 56. Sum of even numbers in range

# for i in range(0,20,2):
#     print(i)

# # 57. Sum of odd numbers in range

# for i in range(1,20,2):
#     print(i)

# 58. Print pattern using numbers

# for i in range(1,5):
#     for j in range(i):
#         print(i ,end=" ")
#     print("")

# rows = 5
# for i in range(1, rows + 1):
#     for j in range(i):
#         print(i, end=" ")
#     print() # Moves to the next line
# 59. Print right-angle triangle pattern

# for i in range(5):
#     for j in range(5):
#         print(i*j,end=" ")
#     print()

# for i in range(5):
#     # j now depends on what row (i) we are currently on
#     for j in range(5):
#         print("*", end=" ")
#     print()


# 60. Print inverted triangle pattern

for i in range(10,0,-1):
    print("*" * i)

rows = 5
for i in range(rows):
    # As i gets bigger, (rows - i) gets smaller
    for j in range(rows - i):
        print("*", end=" ")
    print()



# 61. Check strong number

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def is_strong_number(num):
    temp = num
    sum_of_factorials = 0
    
    while temp > 0:
        digit = temp % 10
        sum_of_factorials += factorial(digit)
        temp //= 10
        
    return sum_of_factorials == num

# Testing
number = 145
if is_strong_number(number):
    print(f"{number} is a Strong Number!")
else:
    print(f"{number} is not a Strong Number.")


import math

def check_strong(n):
    return sum(math.factorial(int(d)) for d in str(n)) == n

print(check_strong(145))


# 62. Find perfect number



# 63. Count digits using loop
# 64. Find max digit in number
# 65. Find min digit in number
# 66. Print table from 1 to 10
# 67. Print prime factors
# 68. Count prime numbers in range
# 69. Print ASCII table
# 70. Convert decimal to binary
# 71. Convert binary to decimal
# 72. Convert decimal to octal
# 73. Convert decimal to hexadecimal
# 74. Find power without ** operator
# 75. Print series: 1 + 2 + 3 + …
# 76. Print series: 1² + 2² + …
# 77. Print series: 1³ + 2³ + …
# 78. Check number is automorphic
# 79. Check number is neon
# 80. Check number is spy
# 81. Print digits vertically
# 82. Sum of digits until single digit
# 83. Print alternate numbers
# 84. Count frequency of digits
# 85. Check number divisible by 5 and 11
# 86. Print table using while loop
# 87. Print reverse table
# 88. Find sum of factorial of digits
# 89. Print pattern using alphabets
# 90. Print hollow square pattern
# 91. Print pyramid pattern
# 92. Count even & odd digits
# 93. Find average of numbers
# 94. Find median of numbers
# 95. Find mode of numbers
# 96. Print first N natural numbers
# 97. Print first N even numbers
# 98. Print first N odd numbers
# 99. Find sum of multiples of 3 or 5
# 100. Print pattern using loop

# ## 🔵 LEVEL 3: Strings (101–150)

# 101. Count words in string
# 102. Find longest word
# 103. Find shortest word
# 104. Reverse words in string
# 105. Check anagram strings
# 106. Remove spaces from string
# 107. Replace character in string
# 108. Count character frequency
# 109. Find duplicate characters
# 110. Remove duplicate characters
# 111. Convert string to uppercase
# 112. Convert string to lowercase
# 113. Toggle case of string
# 114. Capitalize first letter
# 115. Count uppercase letters
# 116. Count lowercase letters
# 117. Count special characters
# 118. Check string contains only digits
# 119. Check string contains only alphabets
# 120. Remove punctuation from string
# 121. Split string into list
# 122. Join list into string
# 123. Find substring position
# 124. Count substring occurrences
# 125. Check string rotation
# 126. Reverse each word
# 127. Find longest palindrome substring
# 128. Sort characters in string
# 129. Remove vowels from string
# 130. Find common characters in two strings
# 131. Check balanced parentheses
# 132. Encode string using Caesar cipher
# 133. Decode Caesar cipher
# 134. Find first non-repeating character
# 135. Find repeating characters
# 136. Convert string to title case
# 137. Check string is pangram
# 138. Remove extra spaces
# 139. Replace multiple spaces with one
# 140. Count sentences in string
# 141. Convert string to snake_case
# 142. Convert string to camelCase
# 143. Find word frequency
# 144. Remove specific word
# 145. Check valid email
# 146. Mask email address
# 147. Mask phone number
# 148. Count emojis in string
# 149. Reverse string using slicing
# 150. Reverse string using loop

# ## 🟣 LEVEL 4: Lists, Tuples, Sets, Dicts (151–220)

# 151. Create a list
# 152. Find sum of list elements
# 153. Find max in list
# 154. Find min in list
# 155. Sort list ascending
# 156. Sort list descending
# 157. Remove duplicates from list
# 158. Find second largest element
# 159. Find second smallest element
# 160. Reverse a list
# 161. Rotate list
# 162. Merge two lists
# 163. Find common elements
# 164. Find unique elements
# 165. Count element frequency
# 166. Split list into chunks
# 167. Flatten nested list
# 168. Find missing number in list
# 169. Find duplicate numbers
# 170. Remove element by index
# 171. Remove element by value
# 172. Check list is palindrome
# 173. Convert list to tuple
# 174. Convert tuple to list
# 175. Count tuple elements
# 176. Find max in tuple
# 177. Find min in tuple
# 178. Create set
# 179. Union of sets
# 180. Intersection of sets
# 181. Difference of sets
# 182. Check subset
# 183. Remove element from set
# 184. Create dictionary
# 185. Add key-value pair
# 186. Remove key from dict
# 187. Update dictionary
# 188. Merge dictionaries
# 189. Sort dictionary by key
# 190. Sort dictionary by value
# 191. Find max value key
# 192. Find min value key
# 193. Count word frequency using dict
# 194. Create dict from two lists
# 195. Invert dictionary
# 196. Check key exists
# 197. Iterate dictionary
# 198. Nested dictionary access
# 199. Sum dictionary values
# 200. Find duplicate values in dict
# 201. Create list of squares
# 202. Create list of evens
# 203. List comprehension with condition
# 204. Dict comprehension
# 205. Set comprehension
# 206. Remove None values
# 207. Filter list using lambda
# 208. Map function example
# 209. Reduce function example
# 210. Zip two lists
# 211. Unzip list
# 212. Enumerate list
# 213. Shuffle list
# 214. Random choice from list
# 215. Sort list of tuples
# 216. Group list elements
# 217. Count occurrences using Counter
# 218. Find most common element
# 219. Convert dict to JSON
# 220. Convert JSON to dict

# ## 🔴 LEVEL 5: Functions, OOP, Files, Advanced (221–300)

# 221. Create a function
# 222. Function with parameters
# 223. Function with return value
# 224. Recursive function
# 225. Lambda function
# 226. Default arguments
# 227. Keyword arguments
# 228. Variable length arguments
# 229. Create a class
# 230. Create object of class
# 231. Use **init** method
# 232. Instance variables
# 233. Class variables
# 234. Inheritance example
# 235. Method overriding
# 236. Multiple inheritance
# 237. Encapsulation example
# 238. Polymorphism example
# 239. Abstract class
# 240. Interface-like behavior
# 241. Read file
# 242. Write file
# 243. Append file
# 244. Count words in file
# 245. Count lines in file
# 246. Copy file content
# 247. Search word in file
# 248. Exception handling
# 249. Custom exception
# 250. Try-except-finally
# 251. Use with statement
# 252. Use datetime module
# 253. Use math module
# 254. Use random module
# 255. Generate OTP
# 256. Password strength checker
# 257. Simple login system
# 258. Command-line calculator
# 259. Todo app (CLI)
# 260. Number guessing game
# 261. Dice rolling simulator
# 262. URL shortener logic
# 263. Email validation program
# 264. Phone number validation
# 265. Simple banking system
# 266. Student management system
# 267. Library management system
# 268. Quiz application
# 269. Chat application logic
# 270. ATM simulation
# 271. File encryption logic
# 272. File decryption logic
# 273. Simple web scraper
# 274. API request using requests
# 275. JSON file reader
# 276. CSV file reader
# 277. CSV file writer
# 278. SQLite database CRUD
# 279. Logging in Python
# 280. Multithreading example
# 281. Multiprocessing example
# 282. Async function example
# 283. Async API call
# 284. Producer-consumer problem
# 285. Rate limiter logic
# 286. Cache using dictionary
# 287. LRU cache implementation
# 288. Retry mechanism
# 289. Background task runner
# 290. Scheduler program
# 291. URL status checker
# 292. Password generator
# 293. Image renaming script
# 294. Folder organizer
# 295. Data validation system
# 296. Configuration loader
# 297. Environment variable reader
# 298. API key manager
# 299. Simple REST API (FastAPI)
# 300. Mini Agentic AI task executor