# Error: mistakes in program is called error/bug/exception
# Also these error in the program that occurs while running the program are called exceptions.
# types:
# 1. syntax error
# syntax: the rules of writing program
# eg: print("hello") // Print{"hello"}
# 2. runtime error: error that occurs during running the program is called runtime error
# 
# 3. logical error

# a=10
# b=0
# print(a/b)

# print("Eg of syntax error")
# a=2
# b=4
# print(a+b)
# for i in range(4):
#     print("hello")
# print("Diff", a-b)
# print("mul", a*b)




# Exception handling: The process of handling an exception is called exception handling
# try:
# except:
# else:
# finally:

# try:
#     a = int(input("ENter first num"))
#     b = int(input("ENter second num"))
#     print(a,b)
#     print(a/b)
# except ValueError:
#     print("Enter valid input")
# except ZeroDivisionError:
#     print("Enter number greater than zero")



# if ram_age > sita_age:
#     print("Ram is older")
# else:
#     print("Sita is older")
# else:
#     print("Run successfully")
# finally:
#     print("I don't care about the errors")

# try:
#     a=10
#     b=0
#     print(a/b)
# except ZeroDivisionError: #Exception
#     print("Divided by zero")


# Name error
# c=0
# print(c)

# Type error
# print(1+"a")

# list = [1,2,3,4]
# print(list[4])

# Q1. Ask the user for two numbers and divide the first by the second. If the second number is zero, 
#       print "Cannot divide by zero!" instead of letting the program crash.

def print_each_num (list):
    for i in list:
        print(i)

print_each_num([10,20])