# How to print anything
# name="ANku"
# print("When name contain anku", name)
# name="Bijay"
# print("When name contain Bijay", name)

# Name = ["Bijay", "Ram", "Shyam"]
# age=10
# print("Python revision")
# print(10)
# print(name)
# print(name, "My name is ", name)
# print("I am", name, "and I am", age, "years old")
# print(f"My name is {name} and my age is {age}")
# print(f"I am {name} and I am {age} years old")

# Variable
# Container which store value. Or It is a name of memory location where values are store
# in variable we can store one value at a time
# We can change the value of variable at any time

# Rule of giving name of variable
# we can use alphbates, number, underscore(_)
# starting letter must be either underscore or alphabate (eg. name, _name)
# Start letter never be number(eg. 1name is invalid variable)
# There should not be space in between the variable name (eg. full name is invalid to be valid fullname or full_name)
# We cannot use keywords as a varibale name (eg. print, input, if, upper, lower, split)
# Variables are case sensitive (note python is case sensitive i.e name and Name or NAme they all are different)

# How to take input from user
# To take input we use input() statement

# subject = input("Enter your fav subject ")
# print("My fav subject is ", subject)
# print(f"My fav subject is {subject}")

# If we take input from input statement then the data type of that data is always string
# means if we take number as input, data type is also string.
# That is why we need to do type casting/ type conversion

# Implicit and another explicit
# Implicit is done by the python interpreter
# Explicit is done by the user itself

# to convert any data into interger we use int()
# syntax: int(variable_name)
# to convert into string we use str()
# syntax: str(variable_name)
# to float we use float()
# syntax: float(variable_name)

# 1j or 1+1j

# string
# subject = "ComputerScienceadbljabfluerfgierlgf"
# print(subject[-3])
# function: function_name(arguments) //call
# syntax:: variable.method()
# print(subject.upper())
# print(subject.lower())
# print("subject".upper())

# name= "     biiijaibhawa" 
# Abha gupta
# print(name.capitalize()) 
# print(name.title())

# print(name.find("i"))
# print(name.count("a"))
# print(name.split("h"))
# print("withou stripe", name)
# print("with stripe", name.strip())

# arthmetic operator
#  a + b (a and b are called operand and + is called operator)
# they are +, -, *, /, ** (power 3**2), % (5%2 = 1)


# Input : what you need (eg: length, breadth, radius, principal, time, rate)
# use the formula and then store the value in a variable
# variable_name = formula
# eg: area = length * breadth
# print the result

# Write a program to find the area of square

# length = int(input("Enter the length of square "))
# Area = length**2
# print(f"The area of the square is {Area}")

# Write a program to find the area of circle
# def area_of_circle(radius):
#     PI = 3.14
#     # radius = int(input("Enter the radius of circle "))
#     area = PI * radius**2
#     print(f"The area of circle is {area}")

# area_of_circle(2)

# for i in range (1,51):
#     area_of_circle(i)


# list1 = ["Bijay", "Ram", "Biju", "shyam", "Radhika", "Laxmi", 1,2,3,4,5,5,6]
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])

# for i in range(0,len(list1)):
#     print(list1[i])

# Write a function to check you are pass or not (pass:; marks >= 35)

def is_pass(marks):
    if(marks>=35):
        print("you are pass")
    else:
        print("you are fail")

# is_pass(23)
# is_pass(23)
# is_pass(23)
# is_pass(23)
# is_pass(23)
# is_pass(23)
# is_pass(23)
# is_pass(23)
# is_pass(23)
# is_pass(23)

# for i in range(1,4):
#     marks = int(input("Enter the mark "))
#     is_pass(23)






# how to define function
# we use keyword def

# syntax: def function_name(paramters):




