# class Animal: 
#     @property               # property -> decorator help to call the method without paranthesis ()
#     def show(self):
#         print("Hello, How are you ?")

# obj = Animal()
# obj.show 


# def decorate(func):
#     def wrapper(a,b):
#         print("the addition to your numbers are : ")
#         func(a,b)
#         print("Thank you ! I hope you liked it")
#     return wrapper


# @decorate
# def addition(a,b):
#     print(f"Your total is {a+b}")

# addition(12,67)




def decorate(func):
    def wrapper(*args):             # ->  *args : will accept numerous arguments in the wrapper function 
        print("the addition to your numbers are : ")
        func(*args)
        print("Thank you ! I hope you liked it")
    return wrapper


@decorate
def addition(a,b,c):
    print(f"Your total is {a+b+c}")

addition(12,67,30)