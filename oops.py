# a = 12
# b = 15
# print(a + b)        # Imperative Approach

# def add (a , b):
#     print(a + b)        # Functional Approach

# add(12,12)
# add(20,30)

############################# Object Oriented Programming Approach (OOP) #############################

# Classes 

class  Animal :
    species = "DOG"                 # Attribute 
    a = 12

    def hello (self):
        print("Hello World")        # Method 

    # print("How are you i am getting initialized")

# obj = Animal()
# print(obj.a)
# print(obj.species)
# obj.hello()

# obj2 = Animal()

# obj3 = Animal()
# obj3.hello()

# Animal()
# print(Animal().a)
# Animal().hello()


# constructors 

class  Animal :
    def __init__(self,type,breed):
        # print(self)
        self.type = type
        self.breed = breed

    def show(self):
        print(f"Your objects are {self.breed},{self.type}")

dog = Animal("Dog","Pamerian")

cat = Animal("Cat","Black")

print(dog.breed)
print(cat.type)
cat.show()