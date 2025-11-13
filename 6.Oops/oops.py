#------ Class & Object ---#
# class Car:
#     print("Object created")
# audi = Car()

#----Class & Attributes -----------------#
# class Room:
#     length = 0.0
#     breadth = 0.0
#
#     def calculate_area(self):
#         print("Area of Room =", self.length * self.breadth)
#
# # create object of Room class
# study_room = Room()
# study_room.length = 42
# study_room.breadth = 30
# study_room.calculate_area()

#------Class,Constructors & Methods------#
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         self.color = "black"
#
#     def display(self):
#         print(self.brand,self.model)
#     def __del__(self):
#         print(self.brand," car deleted")
#
# mycar=Car("Skoda","kushaq")
# hiscar=Car("Benz",2022)
# print("My Car details:")
# mycar.display()
# print("His Car details:")
# hiscar.display()
# del mycar
# del hiscar

#-----------Access Modifier-----------------#
class profile:
    def __init__(self,name,position,salary):
        self.name= name
        self._position=position
        self.__salary= salary
    def get_salary(self):
        return self.__salary
    def emp_profile(self):
        return self.name, self._position, self.__salary

name1=profile("alex","engineer",'$10000')
print(name1.name)
sal= name1.get_salary()
# print (name1.__salary)
print (name1.emp_profile())
print(sal)


#-------------Inheritance--------------#
# class Animal:
#     def eat(self):
#         print("Eating...")
#
# class Dog(Animal):
#     def bark(self):
#         print("Barking...")
#
# mydog=Dog()
# mydog.eat()
# mydog.bark()


#------------Constructor of a child class----------#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#         print("Animal", self.name,"created.")
#
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)  # Call the superclass constructor
#         self.breed = breed
#         print("Dog", self.name, "of breed", self.breed,"created.")
#
# # Creating an instance of the subclass
# my_dog = Dog("Buddy", "Golden Retriever")
# street_dog = Dog("Rogue", "Country")
# print("Name:", street_dog.name,"Breed:", street_dog.breed)