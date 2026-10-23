# import calculation
# from calculation import *
# from calculation import rectangle_area, circle_area
# from module_name import function_name
# from module_name import *
# module.function_name
# print(calculation.rectangle_area())

# print(circle_area())

# import result

# from school.result import percentage
# print(result.perentage(23,50))

# import school
# import result
# from result import avg
# # print(school.result.avg(560,7))
# print(avg(560,7))

# import school
# # import school.result as xyz #alias
# from school.result import *
# print(perentage(100,200))
# import pandas
# data = pandas.DataFrame({
#     "Name": ["Ram", "Sita"],
#     "Age": [20, 21]
# })

# print(data)

# import math
# import random
# import turtle
# from math import sqrt

# from calculation import circle_area
# from calculation import *
# circle_area()
# import calculation
# calculation.circle_area()

# math module
# cos(), sin(), tan(), log(), log10(), pi(), sqrt(), pow(), factorial()
# log stands for logarithm
# log base e
# import math
# print(math.cos(60*(180/math.pi)))
# print(math.sin(60*(180/math.pi)))
# print(math.tan(45*180/math.pi))

# print(math.log10(10))

# PI = 3.14
# area_cicle = math.pi * 7 **2
# print(area_cicle)

# print(math.pi)

# num = 9.5
# print(math.floor(num))
# print(math.ceil(num))
# print(math.sqrt(num))
# print(math.pow(2,3))


# print(num**(1/2))

# num=10 #1*2*3*4*5*6*7*8*9*10
# fact=1
# for i in range(1,11):
#     fact=fact*i
# print(fact)

# print(math.factorial(5))

# print(math.pi)

# print(math.tan(math.pi/4))

# PI =3.14
# radius = int(input("Enter the radius:"))
# area = math.pi*radius**2
# print("Area of circle", area)

import random
# random() = 0,1
# print(random.random())
# randint(0,1)
# print(random.randint(0,3)) #3 included i.e upperlimit is included
# print(random.randrange(0,3)) #upper limit is not included

# students = ["Akriti", "Abha", "Alisha", "Garima","Ankit", "Bibek"]

# print(random.choices(students, weights=[10,20,30,50,60,700], k=3))

# poss = random.random()
# if(poss>=0.5):
#     print("Head")
# else:
#     print("Tail")

dice = random.randrange(1,7)
print("You rolled", dice)