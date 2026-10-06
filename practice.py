# print the rev of a number
# def reverse_number():
#     num = int(input("Enter a number "))
#     rev = 0
#     while num>0:
#         rem = num%10
#         rev=rev*10+rem
#         num=num//10

#     return rev

# print(reverse_number())

# Write a function to calculate area of circle and rectangle
# def circle_area()
#     PI=3.14
# r=int(input("Enter the radius of the circle "))
#     area_circle = Pi*r*2
#     return area_circle


# def circle_area():
#     PI=3.14
#     r=int(input("Enter the radius of the circle"))
#     area_circle = PI*r**2
#     return area_circle

# def rectangle_area():
#     l= int(input("Enter the length "))
#     b=int(input("Enter the breadth "))
#     area_rect = l * b
#     return area_rect

# print(f"Area of circle is {circle_area()} and rectangle is {rectangle_area()}")


# Amstrong number = 123 = 1^3 + 2^3 + 3^3 = 1+8+27=46
# 153 = 1^3 + 5^3 + 3^3 = 1+125+27=153

# To check amstrong number
# def check_amstrong():
#     num = int(input("Enter a number "))
#     original_num = num
#     sum = 0
#     while num>0:
#         rem = num % 10       
#         sum = sum + rem**3       
#         num = num//10      
#     if(original_num==sum):
#         print("The number is amstrong number")
#     else:
#         print("The number is not an amstrong number")

# check_amstrong()

# Write a function to calculate the area of square and volume of a cuboid
# Write a function to check eligibility to vote (condition: must have citizenship and older than 18)
# Write a function to count consonant letter in a word
# Write a function to find greatest among three and two number

# Greatest among two number
# def greatest_two ():
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     if(num1>num2):
#         print("Num1 is greatest")
#     elif(num2>num1):
#         print("num2 is greatest")
#     else:
#         print("num1 and num2 are equal")

# def greatest_three():
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     num3 = int(input("Enter the third number: "))
#     if(num2<num1>num3):
#         print("num1 is greatest")
#     elif(num1<num2>num3):
#         print("num2 is greatest")
#     elif(num1<num3>num2):
#         print("num3 is greatest")
#     else:
#         print("num1, num2 and num3 are equal")

# greatest_two()
# greatest_three()

# list = [1,2,3,4,100,67]
# print(min(list))

# def greatest_three():
#     num = []  
#     num.append(int(input("Enter the first number ")))
#     num.append(int(input("Enter the second number ")))
#     num.append(int(input("Enter the third number ")))
#     print(f"The greatest number is {max(num)}")

# greatest_three()

# def div(a,b):
#     return a//b

# print(div(2,3))

# 0,1,1,2,3
# a=b, b=c c=a+b
# if a and b are the last two term then the third time is c=a+b

# term=1
# a=0
# b=1
# print(a)
# print(b)
# while term<=3:
#     c=a+b
#     print(c)
#     a=b
#     b=c
#     term = term+1

def result(n):
    p=1
    for i in range(1,n+1):
        p=p*i
    return p
n=5
f=result(n)
print(f"The output is {f}")