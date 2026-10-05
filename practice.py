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

def check_amstrong():
    num = int(input("Enter a number "))
    original_num = num
    sum = 0
    while num>0:
        rem = num % 10       
        sum = sum + rem**3       
        num = num//10      
    if(original_num==sum):
        print("The number is amstrong number")
    else:
        print("The number is not an amstrong number")

check_amstrong()

# Write a function to calculate the area of square and volume of a cuboid
# Write a function to check eligibility to vote (condition: must have citizenship and older than 18)
# Write a function to count consonant letter in a word
# Write a function to find greatest among three and two number