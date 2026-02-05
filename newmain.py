# number1=int(input("Enter first number : "))
# number2=int(input("Enter second number : "))
# number3=int(input("Enter third number : "))

# if number1>number2:
#     print(f"Number one is a largest number in three number { number1}")

# elif number2>number3:
#     print(f"Number one is a largest number in three number { number2}")

# else:
#     print(f"Number one is a largest number in three number { number3}")

# number1=int(input("Enter first number : "))
# number2=int(input("Enter second number : "))
# number3=int(input("Enter third number : "))

# if number1>number2:
#     print(f"Number one is a largest number in three number { number1}")

# elif number2>number3:
#     print(f"Number one is a largest number in three number { number2}")

# else:
#     print(f"Number one is a largest number in three number { number3}")

# number1=int(input("Enter first number : "))
# number2=int(input("Enter second number : "))
# number3=int(input("Enter third number : "))

# if number1>number2:
#     print(f"Number one is a largest number in three number { number1}")

# elif number2>number3:
#     print(f"Number one is a largest number in three number { number2}")

# else:
#     print(f"Number one is a largest number in three number { number3}")


# def maxi():
#     number1=int(input("Enter first number : "))
#     number2=int(input("Enter second number : "))
#     number3=int(input("Enter third number : "))

#     if number1>number2:
#         print(f"Number one is a largest number in three number { number1}")

#     elif number2>number3:
#         print(f"Number one is a largest number in three number { number2}")

#     else:
#         print(f"Number one is a largest number in three number { number3}")

# maxi()
# maxi()
# maxi()
# maxi()

# fun=lambda x : x**4
# print(fun(5))


# def newfun(fx,value):
#     return fx*value

# val=newfun(fun(4),55)
# print(f"My value is {val}")


# lst=[1,2,3,4,5,6]

# new_list=[]

# for i in lst:
#     print(i)
#     new_list.append([i**2])

# print(new_list)


# lst=[1,2,3,4,5,6]

# for i in lst:
#     mylist=(i**2)
#     print(mylist)


# mylist=[1,2,3,4,5,6,7,8]

# def function(val):
#     return val**3

# myFun=list(map(function,mylist))
# print(myFun)


# mylist=[1,2,3,4,5,6,7,8]

# # def function(val):
# #     return val**3

# myFun=list(map(lambda x:x**4 ,mylist))
# print(f"This is print List using lambda function {myFun}")


# numbers = [1, 2, 3, 4, 5]

# # map(function, iterable)
# squared = list(map(lambda x: x**2, numbers))

# print(squared) 
# # Output: [1, 4, 9, 16, 25]


# mylist=[1,2,3,4,5,6]

# def myFunction(value):
#     if value%2:
#         print(value)

# numbers = [1, 2, 3, 4, 5]

# # map(function, iterable)
# squared = list(map(lambda x: x**2, numbers))

# print(squared) 
# # Output: 



# mylist=[1, 4, 9, 16, 25]
# my_new_list=[]
# for i in mylist:
#     if i%2==0:
#         my_new_list.append(i)

# print(my_new_list)

# print(4*"*")
# mylist=[1, 4, 9, 16, 25]

# def newFunction(value):
#     if value%2==0:
#         return value

# myfilter=list(filter(newFunction,mylist))
# print(myfilter)

# print("**"*5)

# myfilter=list(filter(lambda x:x%2==0,mylist))
# print(myfilter)


# import functools


# mylist=[1,2,3,4,5,6]
# sum=0
# for i in mylist:
#     sum=sum+i

# print(sum)


# myreduced=functools.reduce(lambda x,y:x+y, mylist)

# print(myreduced)

# list_a = [1, 2, 3.3]
# list_b = [1, 2, 3]


# print(list_a == list_b)

def fact(number):
    fact=1
    for i in range(1,number+1):
        fact=fact*i
    return fact
    

print(fact(10))