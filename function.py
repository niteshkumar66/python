# functions 

# print("Hello how are you ")       # in-built funciton


def greet ():
    print("Hello , Good Morning")

# greet()


def hello(name):
    print(f"Good Morning , {name}")

# hello("Nitesh")

def sum (a , b):
    print(f"Sum is {a + b}")

# sum(4,5)
# sum(45,45)

def helloOnly (name,age):
    print(f"Name is {name} and the age is {age}")

# helloOnly(age = 22 , name = "Nitesh")       # keyword argument (position doesn't matter)


def add (a , b = 45):           # defualt parameter
    print(f"Sum is {a + b}")

# add(30)         # b has a default value 45 and we passed a = 30 => 30 + 45 = > 75
# add( 30 , 40)   # here b has been overwritten by the b = 40 value => 30 + 40 = > 70

def isPallindrome (word):
    rev = ""
    for i in range (len(word)-1, -1, -1):
        rev += word[i]

    if (word == rev):
        print(f"{word} is palindrome")
    else : 
        print(f"{word} is not palindrome")

# isPallindrome("mom")
# isPallindrome("hello")


def helloWorld ():
    return "Hello world , how are you all ? "

print(helloWorld())