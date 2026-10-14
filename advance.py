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




# def decorate(func):
#     def wrapper(*args,**kwargs):             # ->  *args : will accept numerous arguments in the wrapper function 
#         print("the addition to your numbers are : ")
#         func(*args,**kwargs)
#         print("Thank you ! I hope you liked it")
#     return wrapper


# @decorate
# def addition(a,b,c):
#     print(f"Your total is {a+b+c}")

# addition(12,67,30)


# def add(*args):           # for normal arguments -> use single star (*keywords(any)) -> args
#     sum = 0
#     for i in args:
#         sum += i

#     print(sum)

# add(12,14,23,12,55,65)

# store arguments in the form of tuple // no need of args keyword compulsory


# def add(**kwargs):          # for positional arguments -> use double star (**keywords(any)) -> kwargs
#     print(kwargs)

# add(a = 12 , b = 34 , c = 20)

# store arguments in the form of dictonary // no need of kwargs keyword compulsory  


# def information(**kwargs):         
#     print("Your information is : \n")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")

# information(name = "Nitesh" , age = 23 , role = "AI & ML Engineer")



# a = 12
# print("even") if a % 2 == 0 else print("odd")

# l = []
# for i in range(1,21):
#     if i % 2 == 0:
#         l.append(i)

# print(l)


# l = [i for i in range(1,21) if i % 2 == 0]
# print(l)


# l = {i : i**2 for i in range(1,11)}
# print(l)

# unique_even_number = {i*i for i in range(10) if i % 2 == 0}
# print(unique_even_number)


######################### Lambda Function ##########################

# Normal Function 
# def add(a,b):
#     print(a + b)

# add(12 ,13)


# Lambda Function       # store in the variable , act as an object while calling the function 

# addition = lambda a,b : a + b
# print(addition(12 ,14))


# square = lambda x : x**2
# print(square(12))


# check_even = lambda x : "Even" if x % 2 == 0 else "Odd"
# print(check_even(13))


################### MAP #####################

# a = [1,2,3,4,5]

# def double(x):
#     return x * 2

# double = map(double,a)

# # double = map(lambda x : x*2 , a)

# print(list(double))
