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

import pandas as pd

data = pd.DataFrame({
    "Name": ["Ram", "Sita"],
    "Age": [20, 21]
})

print(data)

