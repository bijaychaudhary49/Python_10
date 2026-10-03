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
def sum(a,b):
    
    return a+b, a-b, a*b
var1,var2,var3 = sum(2,3)
print(var1,var2,var3)

# var1=2
# var2=3
# var3=4

# var1,var2,var3 = 2,3,4



# Function is a reusable block of code that can be used at anytime by just calling their name


# Q. Write a function to calculate the area of rectangle.
# Q. Write a fucntion which check whether a number is even or odd.
# Q. Write a function to check greatest among three number
# Q. Write a program to count vowel in a string