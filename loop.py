# cycle = loop

# for loop , while loop
# iteration

# for variable_name in in_which i have to loop (range(), list, tuple, set, dict):

# range functions take 3 three parameter
# range(start, stop, step_value)

# print(list(range(5))) # the last range is never included and always exclued
# print(list(range(1,5))) # the last range is never included and always exclued
# print(list(range(1,5,2))) # the last range is never included and always exclued

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# for i in range(1,11):
#     print("hello world")

# WAP to print first n odd number
# n = int(input("Enter the value of n "))
# for i in range(2,n*2+1,2):
#     print(i)

# for i in range(1,21):
#     if(i%2==1):
#         print(i)

# Write a Python program that loops through the numbers 1 to 20. If the number is odd, print "Fizz"; otherwise, print "Ball"
# for i in range(1,21):
#     if(i%2==0):
#         print(i, "Ball")
#     else:
#         print(i, "Fizz")

# Write a Python program that prints the numbers from 1 to 100. 
# For multiples of 2, print "Fizz" instead of the number; for multiples of 4, print "Buzz"; and for multiples of both 2 and 4, print "FizzBuzz"

# for i in range(1,101):
#     if(i%3==0 and i%5==0):
#         print("FizzBuzz")
#     elif(i%3==0):
#         print("Fizz")
#     elif(i%5==0):
#         print("Buzz")
#     else:
#         print

# num = 9
# print(9**(1/2))

# import pandas as p
# print(p.sqrt(9))

# nested loop = loop inside loop, this is called nested loop
# outer loop = external loop
# inner loop = internal loop


# for i in range(5):
#     for j in range(4 - i, -1, -1):
#         print(j, end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# for i in range(5,0,-1):
#     print("*"*i)

# for loop through list

fruits = ["apple", "banana", "mango", "litchi"]
set = {"apple", "banana", "mango", "litchi"}
tup = ("apple", "banana", "mango", "litchi")
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])

# dict = {
#     "name":"Bijay",
#     "age":23,
#     "address":"Ramgram-10"
# }
# items = dict.items()

# for key,value in items:
#     print(key, value )

# print(list(range(5)))
# for i in range(5):
#     print(i)

# for i in range(4,-1,-1):
#     print(i)


# Write a program to enter name and marks of students in a dictionery and print the name of students who are pass
# Write a program to store number in a list and print the number which are greater than 35

number=[]
n = int(input("Enter the number of number "))
for i in range(n):
    num = int(input("Enter the number "))
    number.append(num)
for x in number:
    if(x>35):
        print(x)

# list = []
# list.append("bijay")
# print(list)
# list = [0,1,2,3,4]

# list[0]=5
# print(list)
# dict["name"]=value



# students={}
# num = int(input("Enter the number of student "))
# for i in range(num):
#     name=input("enter the name of student ")
#     mark=int(input("Enter the mark of student"))
#     students[name]=mark

# for name,marks in students.items():
#      if(marks>=35):
#           print(name)

# for num in list:

# for i in range(5):
    # for j in range(4,i-1,-1):
    #     print(j, end='')
    # print()


# for i in range(5):
#     for j in range(2):
#         print(i,j)


# for i in range(5):
#     for j in range(i+1):
#         print(j, end=" ")
#     print()

# for variable_name in sequencce (range(),str,list,tup,set,dict)

# name=["Bijay","ram","shyam","hari","sita"]

# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])
# print(list[4])

# for i in name:
#     print(i)

# details = {
#     "name":"Bijay",
#     "age":23,
#     "address":"Manjhariya"
# }

# for key,value in dict.items():
    # print(key,":",value)

# print(details.items()) 
# for key,value in details.items():
#     if(key=="name"):
#
#          print(value)
# n input
# n=5
# fact=1
# if(n==0):
#     fact=1
# else:
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)


# Q.Write a program to print sum of even number and odd number between 1 to 100
# Output
# Sum of even number = value
# Sum of odd number = value

# for loop and while loop

# while condition:
    # block of stament

# using while loop print first 10 natural number
# for x in range(1,11):
#     print(x)

# students = [] #["Abha","Akriti","Jyoti","Garima",]
# i = input("Press c to continue")
# while i.lower()=="c":    
#     name=input("Enter the name of students ")
#     students.append(name)
#     i = input("press c to continue ")

# students.sort(reverse=True)
# for student in students:
#     print(student)

# i=0
# while i<3:
#     print(students[i])
#     i+=1
