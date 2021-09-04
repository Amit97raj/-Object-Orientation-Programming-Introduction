# Python Basics Chapter 16:
# =========================

# 1. Object Orientation Programming Introduction

# Common topic in almost all popular programming languages (Python, 
# C++, Java) with common idea with different syntax.
# OOP is just a style / way to write a code.
# Very helpful in creating real world programs.

# Most common words in OOP - 

# Class
# Object (instance)
# Method.

# Example -

# List Class
# List Object 
# List Method.

# l = [1, 2, 3, 4]
# l.append(5)

# 2. OOP Class

# __init__() method / constructor
# functions inside the class are known as methods.
# self represents the object of class.

# class Person:
#     def __init__(self, first_name, last_name, age):
#         print("init method / constructor get called")
        
#         # instance variables
#         self.first = first_name
#         self.last = last_name
#         self.age = age

# p1 = Person("Anshul", "Garg", 22)
# p2 = Person("Anurag", "Chapperwal", 24)

# print(p1.first)
# print(p2.first)

# 3. OOP Exercise - 1

# Create a Laptop class with attributes like brand name, model name,
# and price.
# Create two objects / instances of your laptop class. 

# 4. OOP Exercise - 1 Solution

# class Laptop:
#     def __init__(self, brand_name, model_name, price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
        
#         self.full_name = self.brand_name + " " + self.model_name

# l1 = Laptop("HP", "Pavillion 15", 80000)
# l2 = Laptop("Lenovo", "Legion Y540", 75000)

# print(l1.full_name)
# print(l2.full_name)

# 5. OOP Instance Methods

# class Person:
#     def __init__(self, first_name, last_name, age):
#         # instance variables
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
    
#     # instance method
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"

#     # instance method
#     def is_above_18(self):
#         return f"{self.age > 18}"

# p1 = Person("Anshul", "Garg", 22)
# p2 = Person("Anurag", "Chapperwal", 24)

# print(p1.full_name())
# print(p2.full_name())

# print(Person.full_name(p1))
# print(Person.full_name(p2))

# print(p1.is_above_18())
# print(p2.is_above_18())

# 6. OOP Exercise - 2

# Add apply_discount method to the Laptop class. 

# class Laptop:
#     def __init__(self, brand_name, model_name, price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
        
#         self.full_name = self.brand_name + " " + self.model_name

# l1 = Laptop("HP", "Pavillion 15", 80000)

# print(l1.apply_discount(40))

# 7. OOP Exercise - 2 Solution

# class Laptop:
#     def __init__(self, brand_name, model_name, price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
#         self.full_name = self.brand_name + " " + self.model_name
    
#     def apply_discount(self, discount):
#         return f"Effective Price : {self.price - ((discount / 100) * self.price)}"

# l1 = Laptop("HP", "Pavillion 15", 80000)

# print(l1.apply_discount(40))

# 8. Class Variable Part - 1

# class Circle:
#     def __init__(self, r, pi):
#         self.r = r
#         self.pi = pi
    
#     def calc_circumference(self):
#         return 2 * self.pi * self.r

#     def calc_area(self):
#         return self.pi * (self.r ** 2)

# class Circle:
#     # class variable
#     pi = 3.14

#     def __init__(self, r):
#         # instance variables
#         self.r = r
    
#     # instance method
#     def calc_circumference(self):
#         return 2 * Circle.pi * self.r

#     # instance method
#     def calc_area(self):
#         return Circle.pi * (self.r ** 2)

# c1 = Circle(4)
# c2 = Circle(5)

# print(c1.calc_circumference())
# print(c1.calc_area())

# print(c2.calc_circumference())
# print(c2.calc_area())

# class Laptop:
#     discount = 10
    
#     def __init__(self, brand_name, model_name, price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
#         self.full_name = self.brand_name + " " + self.model_name
    
#     def apply_discount(self):
#         return f"{self.price - ((Laptop.discount / 100) * self.price)}"

# l1 = Laptop("HP", "Pavillion 15", 80000)

# print(l1.apply_discount())

# 9. Class Variable Part - 2

# class Laptop:
#     discount = 10
    
#     def __init__(self, brand_name, model_name, price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
#         self.full_name = self.brand_name + " " + self.model_name
    
#     def apply_discount(self):
#         return f"{self.price - ((Laptop.discount / 100) * self.price)}"

# l1 = Laptop("HP", "Pavillion 15", 80000)
# print(l1.apply_discount())

# class Laptop:
#     discount = 10
    
#     def __init__(self, brand_name, model_name, price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
#         self.full_name = self.brand_name + " " + self.model_name
    
#     def apply_discount(self):
        # return self.price - ((self.discount / 100) * self.price)

# Laptop.discount = 20
# l1 = Laptop("HP", "Pavillion 15", 80000)
# l2 = Laptop("Lenovo", "Legion Y540", 75000)

# print(l1.apply_discount())
# print(l2.apply_discount())

# print(l1.__dict__)

# l2.discount = 30
# print(l2.__dict__)
# print(l2.apply_discount())

# 10. OOP Exercise - 3

# Count instances of Person class.

# class Person:
#     pass

# p1 = Person()

# print(Person.count_instance)

# 11. OOP Exercise - 3 Solution

# class Person:
#     count_instance = 0
    
#     def __init__(self):
#         Person.count_instance += 1

# p1 = Person()
# p2 = Person()
# p3 = Person()

# print(Person.count_instance)

# 12. OOP Class Methods

# class Person:
#     # class variable / class attribute
#     count_instance = 0
    
#     def __init__(self, first_name, last_name, age):
#         Person.count_instance += 1
#         # instance variables
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     # class method 
#     @classmethod
#     def count_instances(cls):
#         return f"You have created {cls.count_instance} instances of {cls.__name__} class."
    
# #     # instance method
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"

# #     # instance method
#     def is_above_18(self):
#         return f"{self.age > 18}"

# p1 = Person("Anshul", "Garg", 22)
# p2 = Person("Anurag", "Chapperwal", 24)

# # print(Person.count_instance)

# print(Person.count_instances())

# print(p1.count_instances())
# print(p2.count_instances())

# 13. Class Methods As a Constructor

# class Person:
#     # class variable / class attribute
#     count_instance = 0
    
#     def __init__(self, first_name, last_name, age):
#         Person.count_instance += 1
        
#         # instance variables
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
    
#     # class method as a constructor
#     @classmethod
#     def my_constructor(cls, string):
#         first, last, age = string.split()
#         return cls(first, last, age) # Person("Anshul", "Garg", 22)

#     # class method 
#     @classmethod
#     def count_instances(cls):
#         return f"You have created {cls.count_instance} instances of {cls.__name__} class."
    
#     # instance method
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"

#     # instance method
#     def is_above_18(self):
#         return f"{self.age > 18}"

# # p1 = Person("Anshul", "Garg", 22)
# # # p2 = Person("Anurag", "Chapperwal", 24)

# # p3 = Person.my_constructor("Anshul Garg 22")
# # p4 = Person.my_constructor("Anurag Chapperwal 24")

# # print(p1.full_name())
# # # print(p2.full_name())

# print(p3.full_name())
# print(p4.full_name())

# 14. OOP Static Method

class Person:
    # class variable / class attribute
    count_instance = 0

    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    # static method
    @staticmethod
    def welcome():
        return f"Welcome To My Class !!"
    
    # class method as a constructor
    @classmethod
    def my_constructor(cls, string):
        first, last, age = string.split()
        return cls(first, last, age)

    # class method 
    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} class."
    
    # instance method
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # instance method
    def is_above_18(self):
        return f"{self.age > 18}"


p1 = Person("Anshul", "Garg", 22)

print(Person.welcome())
print(p1.welcome())

# 15. Encapsulation, Abstraction, Naming Convention, Name Mangling

# In python - everything is public but there are some conventions for 
# indicating a thing as private just for other developers :

# Example -

# _name (convention for private name)
# __name__ (special / dunder / magic methods)
# __name (name mangling)

# class Phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model 
#         self.price = price
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
#     def make_a_call(self, phone_number):
#         return f"Calling {phone_number} ..."
    
#     def send_message(self, msg):
#         return f"Sending {msg} ..."

# class Phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model 
#         self._price = price
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
#     def make_a_call(self, phone_number):
#         return f"Calling {phone_number} ..."
    
#     def send_message(self, msg):
#         return f"Sending {msg} ..."

# class Phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model 
#         self.__price = price
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
#     def make_a_call(self, phone_number):
#         return f"Calling {phone_number} ..."
    
#     def send_message(self, msg):
#         return f"Sending {msg} ..."

# p1 = Phone("Samsung", "Galaxy S20 Fan Edition", 49999)

# # print(p1.full_name())
# # print(p1.make_a_call(9468097841))
# # print(p1.send_message("Hello"))

# # print(p1.__price)

# # p1.__price = 39999
# # print(p1.__price)

# # print(p1.__price)

# # print(p1.__dict__)

# print(p1._Phone__price)

# p1._Phone__price = 39999
# print(p1._Phone__price)

# 16. OOP Property And Setter Decorator

# class Phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self._price = max(price, 0)
#         # self.full_specs = f"{self.brand} {self.model} and Price is {self._price}"
    
#     def full_specs(self):
#         return f"{self.brand} {self.model} and Price is {self._price}"

#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
#     def make_a_call(self, phone_number):
#         return f"Calling {phone_number} ..."
    
#     def send_message(self, msg):
#         return f"Sending {msg} ..."

# class Phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self._price = max(price, 0)
#         # self.full_specs = f"{self.brand} {self.model} and Price is {self._price}"
    
#     @property
#     def full_specs(self):
#         return f"{self.brand} {self.model} and Price is {self._price}"

#     @property
#     def price(self):
#         return self._price
    
#     @price.setter
#     def price(self, cost):
#         self._price = max(self._price, 0)

#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
#     def make_a_call(self, phone_number):
#         return f"Calling {phone_number} ..."
    
#     def send_message(self, msg):
#         return f"Sending {msg} ..."

# p1 = Phone("Samsung", "Galaxy S20 Fan Edition", 49999)

# print(p1.brand)
# print(p1.model)

# p1._price = 39999

# print(p1._price)
# print(p1.full_specs)

# print(p1._price)
# print(p1.full_specs())

# print(p1.full_specs)

# print(p1.price)

# p1._price = -39999
# print(p1._price)
# print(p1.full_specs)

# 17. Inheritance Introduction

# class Phone: 
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model 
#         self._price = max(price, 0)
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"

# class Smartphone:
#     def __init__(self, brand, model, price, ram, internal, rear):
#         self.brand = brand
#         self.model = model 
#         self._price = max(price, 0)
#         self.ram = ram
#         self.internal = internal
#         self.rear = rear
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"

# class Phone: # base class / parent class
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model 
#         self._price = max(price, 0)
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"

# class Smartphone(Phone): # derived class / child class
#     def __init__(self, brand, model, price, ram, internal, rear):
        
#         # Phone.__init__(self, brand, model, price)
#         super().__init__(brand, model, price)

#         self.ram = ram
#         self.internal = internal
#         self.rear = rear

# p1 = Phone("Nokia", "1100", 999)
# s1 = Smartphone("Samsung", "Galaxy S20 Fan Edition", 49999, "8GB", "128GB", "32MP")

# print(p1.full_name())
# print(s1.full_name())

# 18. Multilevel Inheritance, MRO, Method Overriding

# MRO -> Method Resolution Order

# class Phone: # base class / parent class
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model 
#         self._price = max(price, 0)
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"

# class Smartphone(Phone): # derived class / child class
#     def __init__(self, brand, model, price, ram, internal, rear):
        
#         super().__init__(brand, model, price)

#         self.ram = ram
#         self.internal = internal
#         self.rear = rear
    
#     # Method Overriding
#     def full_name(self):
#         return f"{self.brand} {self.model} and Price is {self._price}"

# class Flagship(Smartphone): # derived class / child class
#     def __init__(self, brand, model, price, ram, internal, rear, front):

#         super().__init__(brand, model, price, ram, internal, rear)

#         self.front = front
    
#     # Method Overriding
#     def full_name(self):
#         return f"{self.brand} {self.model} with Front Camera of {self.front} and Price is {self._price}"

# p1 = Phone("Nokia", "1100", 999)
# s1 = Smartphone("Samsung", "Galaxy S20 Fan Edition", 49999, "8GB", "128GB", "32MP")
# f1 = Flagship("Samsung", "Note 20 Ultra", 149999, "16GB", "256GB", "64MP", "32MP")

# print(p1.full_name())
# print(s1.full_name())
# print(f1.full_name())

# print(help(Flagship))

# print(p1.full_name())
# print(s1.full_name())
# print(f1.full_name())

# isinstance(), issubclass()

# print(isinstance(p1, Phone))
# print(isinstance(s1, Phone))
# print(isinstance(f1, Phone))

# print(isinstance(f1, Smartphone))
# print(isinstance(s1, Phone))
# print(isinstance(f1, Phone))

# print(issubclass(Flagship, Smartphone))
# print(issubclass(Smartphone, Phone))
# print(issubclass(Flagship, Phone))

# 19. Multiple Inheritance

# class A:

#     def class_A_method(self):
#         return f"I\'m just a class A method"
    
#     def hello(self):
#         return f"Hello from class A"

# class B:

#     def class_B_method(self):
#         return f"I\'m just a class B method"
    
#     def hello(self):
#         return f"Hello from class B"

# # class C(A,B):
# #     pass

# class C(B,A):
#     pass

# # a = A()
# # b = B()

# c = C()

# # print(a.class_A_method())
# # print(b.class_B_method())

# # print(c.class_A_method())
# # print(c.class_B_method())

# # print(c.hello())

# # print(help(C))

# # print(C.mro())

# print(C.__mro__)

# 20. Special / Magic / Dunder Method, Operator Overloading, Polymorphism

# class Phone: # base class / parent class
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model 
#         self._price = max(price, 0)
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"

#     # special magic / dunder method
#     # def __repr__(self):
#     #     return f"{self.brand} {self.model}"
    
#     # special magic / dunder method
#     def __str__(self):
#         return f"{self.brand} {self.model}"

# class Phone: # base class / parent class
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model 
#         self._price = max(price, 0)
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"

#     # special magic / dunder method
#     def __str__(self):
#         return f"{self.brand} {self.model} and Price is {self._price}"

#     # special magic / dunder method
#     def __repr__(self):
#         return f"Phone(\'{self.brand}\', \'{self.model}\', {self._price})"
    
#     # special magic / dunder method
#     def __len__(self):
#         return len(self.full_name())
    
#     # special magic / dunder method, operator overloading
#     def __add__(self, other):
#         return self._price + other._price

# p1 = Phone("Nokia", "1100", 999)
# p2 = Phone("Nokia", "3300", 1999)

# print(p1)

# print(str(p1))
# print(repr(p1))

# print(p1.__str__())
# print(p1.__repr__())

# print(len(p1))
# print(p1.__len__())

# print(p1 + p2)
