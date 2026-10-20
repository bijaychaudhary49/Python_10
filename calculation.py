def rectangle_area():
    l= int(input("Enter the length "))
    b=int(input("Enter the breadth "))
    area_rect = l * b
    return area_rect

def circle_area():
    PI=3.14
    r=int(input("Enter the radius of the circle"))
    area_circle = PI*r**2
    return area_circle

def reverse_number():
    num = int(input("Enter a number "))
    rev = 0
    while num>0:
        rem = num%10
        rev=rev*10+rem
        num=num//10

    return rev