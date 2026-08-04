# IF else 

# a = 13

# if (a > 10) : 
#     print("I will do task A ")
# else : 
#     print("I will do task B")

# money = int(input("please provide me the money : "))

# if money == 10 : 
#     print("I will hava a choco bar ice cream")
# elif money == 20 :
#     print("I will have a manogo dolly")
# elif money == 30 :
#     print("I will hava a frosty")
# else :
#     print("I will have a cone")


# gender = input("Enter your gender as M and F : ")
# if (gender == 'M'):
#     print("Good Morning Sir")
# elif (gender == 'F') : 
#     print("Good Morning Ma'am")
# else :
#     print("Good Morning")


# num = int(input("Enter a number : "))
# if (num % 2 == 0):
#     print("Even Number")
# else : 
#     print("Odd Number")


# name = input("Enter your name : ")
# age = int(input ("Enter your age : "))

# if (age >= 18 ):
#     print(f"Hello {name}, You are Eligible to Vote")
# else : 
#     print(f"Hello {name}, You are not Eligible to Vote")


# year = int(input("Enter the year : "))
# if (year % 4 == 0):
#     print(f"{year} is a leap year")
# else : 
#     print(f"{year} is not a leap year")


temp = float(input("Enter temperature in celcius : "))
if (temp < 0):
    print("Freezing Cold")
elif (temp >= 0 and temp < 10):
    print("Very Cold")
elif (temp >= 10 and temp < 20):
    print("Cold")
elif (temp >= 20 and temp < 30):
    print("Pleasant")
elif (temp >= 30 and temp < 40):
    print("Hot")
else : 
    print("Very Hot")