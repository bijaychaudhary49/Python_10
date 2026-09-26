# if-else
# if-elif-else
# SLC = "fail"
# if(SLC == "pass"):
#     print("Eligible to study +2")
# else:
#     print("Not eligible to study +2")

# Write a program to differentiate a person eligible to vote or not
# age = int(input("Enter your age "))
# if (age>=18):
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")

# start point: Bus stop - 25
# upto sukrauli = 25
# hakui = 30
# Bhairahwa = 90
# bhairahwa to butwal = 80

destination = input("Enter your destination")
if(destination.lower() == "sukrauli"):
    print("Your fare is 25 rupees")
elif(destination.lower()=="hakui"):
    print(f"your fare is {30} rupees")
elif(destination.lower()== "bhairahawa"):
    print(f"Your fare is {90} rupees")
elif(destination.lower()=="butwal"):
    print(f"Your fare is {90+80} rupees")
else:
    print("You choose wrong destination")

