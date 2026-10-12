# a = 12
# b = 15
# print(a + b)        # Imperative Approach

# def add (a , b):
#     print(a + b)        # Functional Approach

# add(12,12)
# add(20,30)

############################# Object Oriented Programming Approach (OOP) #############################

# Classes 

# class  Animal :
#     species = "DOG"                 # Attribute 
#     a = 12

#     def hello (self):
#         print("Hello World")        # Method 

#     print("How are you i am getting initialized")

# print(Animal().species)

# Animal().hello()

# obj = Animal()        # this is an object : has all power of the Animal class
# print(obj.a)
# print(obj.species)
# obj.hello()

# obj2 = Animal()

# obj3 = Animal()
# obj3.hello()

# Animal()
# print(Animal().a)
# Animal().hello()


##################### constructors #######################

# class  Animal :
#     def __init__(self,type,breed):      # self hold the location of the object 
#         print(self)
#         self.type = type                # location.type = type (attribute)
#         self.breed = breed

#     def show(self):
#         print(f"Your object details are {self.breed},{self.type}") 

# dog = Animal("Dog","Pamerian")

# cat = Animal("Cat","Black")

# print(dog.breed)
# print(cat.type)
# cat.show()
# dog.show()


# class Animal : 
#     name = "Lion"               # class attribute  

#     def __init__(self,age):
#         self.age = age          # instance attribute : attribute created using objexct (self : target object location)

#     def show (self):            # instance method
#         print(f"How are you ?? , your age is {self.age} ")        

#     @classmethod                # Decorator 
#     def hello(cls):             # avoid -> self , use -> cls : target the location of class not object
#         print("How are you brother??")

#     @staticmethod               # this is the simple method , no need of cls or self
#     def hii():
#         print("How are you ? hope good ! ")

# obj = Animal(12)

# obj.show()
# obj.hello()         # classmethod doesnot require parameter bcz target the class and class not accept parameter , objects do 
# obj.hii()

####################### INHERITANCE ######################

# class Parent:
#     pass 

# class Child(Parent):
#     pass

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
# animal1.show()

# person1 = Human("Nitesh",23)
# person1.show()

####################### Multiple Inheritance #########################

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


# obj = Robots("Nitesh")        # the order of inheritance is Animal first : hence asking name only

# obj = Robots("Nitesh",23)     # the order of inheritance is Human first : hence asking name & age both

# print(obj.name1 )
# print(obj.name2)
# print(obj.name3)

######################## Multilevel Inheritance #######################

# class Factory:
#     def __init__(self, material, zip):
#         self.material = material
#         self.zip = zip

# class Bhopal_Factory(Factory):
#     def __init__(self, material, zip, color):
#         super().__init__(material, zip)
#         self.color = color

# class Pune_Factory(Bhopal_Factory):
#     def __init__(self, material, zip, color, pocket):
#         super().__init__(material, zip, color)
#         self.pocket = pocket

#     def show(self):
#         print(f"The Bag includes material = {self.material}, zips = {self.zip} , color = {self.color} , pockets = {self.pocket}")


# obj = Pune_Factory("Leather",3,"Black",3)
# print(obj)
# print(obj.material)
# obj.show()


############################ Polymorphism in OOPS #############################

# same name having Many forms 


# def show ():
#     print("How are you ?")

# def show ():                        # function override in python automatically
#     print("You are Best")

# show()


# class Animal:
#     def show(self):
#         print("Hello I am Nitesh")


# class Human (Animal):
#     def show(self):
#         print("How are you ?")

# obj = Human()

# obj.show()          # method overriding : human show() method override the animal show() method 

# Method Overloading is not supported by the python


## Duck Typing 

# class Animal:
#     def show (self):
#         print("I am showing")

# class Human:
#     def show (self):
#         print("Hello , I am also showing")

# obj = Animal()
# obj2 = Human()

# obj.show()
# obj2.show()


######################## Encapsulation #######################

# class Factory:
#     _a = "pune"             # protected variable use (underscore _ )

#     def show(self):
#         print("Hello , I am a pune factory")

# obj = Factory()

# # obj.show()

# class Bhopal (Factory):
#     def show2(self):
#         print(super()._a)       # not work in python (protected access modifier)

# obj = Bhopal()
# obj.show2()


# class Factory:
#     __a = "pune"             # private variable use (double underscore __ )

#     def __show(self):
#         print("Hello , I am a pune factory")

# obj = Factory()

# # obj.show()

# class Bhopal (Factory):
#     def show2(self):
#         print(super()._a)       # No one can access the method or variable

# obj = Bhopal()
# obj.show2()


# class Factory :
#     __a = "Bhopal"
#                                     # accessing inside the class , outside cannot be access not can change the value
#     def show (self):
#         print(Factory.__a)

# obj = Factory()

# obj.show()


####################### Abstraction ##########################

# from abc import ABC , abstractmethod

# class Abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass

#     @abstractmethod
#     def area(self):
#         pass


# class Square(Abstract):
#     def __init__(self,side):
#         self.side = side

#     def perimeter(self):
#             print("I have calculated")
    
#     def area(self):
#         print("I have created")


# class Circle(Abstract):
#     def __init__(self,radius):
#         self.radius = radius

#     def perimeter(self):
#         print("I have calculated")

#     def area(self):
#         print("I have created")


# obj = Circle(7)
# obj2 = Square(4)

# obj.area()


####################### Dunder Methods #####################

# Dunder means double underscore (__)
# Those special methods which are created with double underscore (__)

# class Person:
#     def __init__(self,name):
#         self.name = name 

# p = Person("Ravi")
# print(p.name)


# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"How are you and your name is {self.name}"

#     def __add__(self, other):
#         return f"Your sum of ages are {self.age + other.age}"


# obj = Animal("Lion",25)
# obj2 = Animal("Dolphin",20)

# print(obj + obj2)


# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"How are you and your name is {self.name}"

#     def __add__(self, other):
#         sum = 0
#         for i in other:
#             sum = sum + i.age

#         return f"Your sum of ages are {self.age + sum}"


# obj = Animal("Lion",25)
# obj2 = Animal("Dolphin",20)
# obj3 = Animal("Deer",15)

# print(obj + (obj2,obj3))
