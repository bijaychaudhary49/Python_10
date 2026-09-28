# Operator: They are the symbols that are used to perform operation on an operand
# eg = a + b. here + is an operator and a, b are operand
# a > b

# Arthematic operator. +, -, *, /, **, %, // 

# print(3/2)  1.5
# print(3//2) # 1
#  a=b //in maths
# x = 10
# x **= 5 # x = x ** 5
# print(x)


# Comparision operator: compare value
# == : check whether the value are equal or not

# a = 6
# b = 6

# print(a!=b)

# Logical operator: and, or, not
# let us suppose p and q. p is true and q true

# 
# print(True and True) #True
# print(True and False) #False
# print(False and True) #False
# print(False and False) #False

# print(True or False) #True
# print(False or True) #True
# print(True or True) #True
# print(False or False) #False

# print(not True) #False
# print(not False) #True

# Check whether the input letter is vowel or consonant
# ltr = input("Enter a single alphabet letter ") #A
# ltr = ltr.lower() #a
# if(ltr == "a" or ltr == "e" or ltr == "i" or ltr =="o" or ltr == "u"):
#     print("The letter you entered is vowel letter")
# else:
#     print("The letter you entered is consonant")

# 0<a and 100>a

num = int(input("ENter a number "))
if(num>0 and num<100):
    print("The number lies in between 0 and 100")
else:
    print("The number lies beyond the range")