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

# class  Animal :
#     def __init__(self,type,breed):
#         # print(self)
#         self.type = type
#         self.breed = breed

#     def show(self):
#         print(f"Your objects are {self.breed},{self.type}")

# dog = Animal("Dog","Pamerian")

# cat = Animal("Cat","Black")

# print(dog.breed)
# print(cat.type)
# cat.show()
# dog.show()

# class Animal : 
#     name = "Lion"               # class attribute  

#     def __init__(self,age):
#         self.age = age          # instance attribute 

#     def show (self):
#         print(f"How are you ?? , your age is {self.age} ")        # instance method

#     @classmethod
#     def hello(cls):
#         print("How are you brother??")

#     @staticmethod
#     def hii():
#         print("How are you ? hope good ! ")

# obj = Animal(12)

# obj.show()
# obj.hello()
# obj.hii()

# class FactoryMumbai:                                # parent class / super class
#     a = "I am a attribute mentioned inside the factory Mumbai"
#     def hello (self):
#         print("Hello i am a method mentioned inside factory Mumbai")

# class FactoryPune (FactoryMumbai):                  # child class / sub class
#     pass

# obj = FactoryMumbai()
# obj2 = FactoryPune()
# print(obj.a)
# obj2.hello()


# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def show (self):
#         print(f"Hello your name is {self.name}")

# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age 

#     def show (self):
#             print(f"Hello your name is {self.name},{self.age}")


# animal1 = Animal("Lion")
# # animal1.show()

# person1 = Human("Nitesh",23)
# person1.show()


# class Animal:
#     name1 = "Lion"

#     def __init__(self,name):
#         pass

# class Human:
#     name2 = "Nitesh"

#     def __init__(self,name,age):
#         pass

# class Robots(Animal,Human):
#     name3 = "Charlie123"


# obj = Robots("Nitesh")

# print(obj.name1 )
# print(obj.name2)
# print(obj.name3)


# class Factory :
#     def __init__(self, material, zip):
#         self.material = material
#         self.zip = zip

# class Bhopal_Factory(Factory):
#     def __init__(self, material, zip,color):
#         super().__init__(material, zip)
#         self.color = color

# class Pune_Factory(Bhopal_Factory):
#     def __init__(self, material, zip, color,pocket):
#         super().__init__(material, zip, color)
#         self.pocket = pocket


# obj = Pune_Factory("Leather",3,"Black",3)
# print(obj)