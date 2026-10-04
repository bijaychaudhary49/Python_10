# def sum():   
#     num1 = int(input("Enter first number: ")) #2
#     num2 = int(input("Enter second number: ")) #3
#     sum = num1 + num2
#     # print("Sum of num1 and num2 =", sum)
#     print(f"Sum of {num1} and {num2} is {sum}")

# sum()
# sum()
# sum()
# sum()
# sum()

# to define function we use keyword "def" that mean define
# syntax: def function_name(parameter1, parameter2)
            # block of code
# To use a function, we have to call the function
# syntax: function_name(argument1, argument2)

# Types of function
# Functions are of two types: In-built function, Userdefined function
# Inbuilt function: input(), print(), len(), int(), float(), str() etc
# user defined function: these are the functions that are defined by the user based upon their need

# Parameters and argument
# Parameter: The value/variable that we pass while defining the function
# Argument: The actual value/variable that we pass while calling the function

# def greet(name):
#     print("Hello!", name)

# greet("Bijay")

# Types of arguments
# 3types: Positional argument

# def sum(a,b):
#     print(f"value of a is {a} and value of b is {b}")
#     print(a+b)

# sum(2,3)

# keyword argument

# def sum(a,b):
#     print(f"value of a is {a} and value of b is {b}")
#     print(a+b)

# sum(b=3, a=2)

# Default argument
# def sum(a=2,b=3):
#     print(f"value of a is {a} and value of b is {b}")
#     print(a+b)
# sum()

# def sum(*var):
#     s=0
#     for value in var:
#         s+=value
#     print(s)

# sum(a=2,b=3)

# Return statement
# def sum(a,b):
    
#     return a+b, a-b, a*b
# var1,var2,var3 = sum(2,3)
# print(var1,var2,var3)

# var1=2
# var2=3
# var3=4

# var1,var2,var3 = 2,3,4



# Function is a reusable block of code that can be used at anytime by just calling their name


# Q. Write a function to calculate the area of rectangle.
# Q. Write a fucntion which check whether a number is even or odd.
# Q. Write a function to check greatest among three number
# Q. Write a program to count vowel in a string

# def rect_area(l,b):
#     area = l*b
#     print(area)
# print(rect_area(2,3))
# rect_area(2,3)

# def even_odd():
#     num = int(input("Enter a number "))
#     if(num%2==0):
#        return ("Even number")
#     else:
#        return ("Odd number")

# # result = even_odd(6)
# print(even_odd())


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# def greates_num():
#     if(num1>num2 and num1>num3):
#         return (f"{num1} is greatest")
#     elif(num2>num3 and num2>num1):
#         return (f"{num2} is greatest")
#     elif(num3>num1 and num3>num2):
#         return (f"{num3} is greatest")    
#     else:
#         return ("They all are equal")
    
# result=greates_num()
# print(result)

# str="Bijay"
# vowel_count = 0
# for i in str:
#     # print(i)
#     if(i.lower()=='a' or i.lower()=='e'or i.lower()=='i' or i.lower()=='o' or i.lower()=='u'):
#         vowel_count += 1

# print("Number of vowel letter in", str, "is", vowel_count)
# print(f"Number of vowel letter in {str} is {vowel_count}")

# scope in python/programming: scope are the region or area or part of program where a variable can be accessed or used.
# python: 4 types of scope
# 1. Local scope variable: These are the variable that are defined inside a function and can be accessed or used inside a function only
# 2. Global scope variable: These are the variable that are defined outside the function and can be accessed anypart of the program
# 3. Enclosing scope: nested function ma occur hunxa. these are the variable that are defined in outer loop and can be accessed inside the inner function
# 4. Built-in scope

# x=10
# def scope():
#     print(x)

# print(x)

# scope()

# def outer_func():
#     x=10
#     def inner_func():
#         print(x)
#     inner_func()

# outer_func()

# print(), input(), len(), int(), float(), str(), type()

def sum(a=4,b=5):
    c=a+b
    print(c)

sum(2,3)