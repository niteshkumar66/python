# Errors 

# print("Hello World"           # Syntax error

# for i in range (21):
# print("Hello")                  # Indentational error

# Tab error


# Exceptions : Other Unexpected or unwanted error and pause the flow of program

# a = int (input ("Tell you number : "))
# print(10/a)                             # Arithmetic Exception : Zero division error 

# print("Okay I have done the division")


# a = input("Enter the number : ")
# try:
#     print(10/a)
# except Exception as err : 
#     print(f"Sorry, there is an error as {err}")



# a = int(input("Enter the number : "))
# try:
#     print(10/a)
# except Exception as err : 
#     print(f"Sorry, there is an error as {err}")
# else :
#     print("Good, there is no error")
# finally:
#     print("I will run the code no matter what")

# print("Okay i have done the division")


age = int(input("Tell your age : "))
try:
    if age < 10 or age > 18 :
        raise ValueError("Your age must be between 10 to 18")       # Raise error by our own 
    else : 
        print("Welcome to the club")
except Exception as err:
    print(f"an error occured as {err}")

print("The club will start soon")
