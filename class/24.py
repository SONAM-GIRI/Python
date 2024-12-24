"""
Abstraction:-

it is one of the pillar of oops which is used to hide the implementaion of code by showing only essential details
for acheiving the abstraction we have to create abstract class
for making class as abstract we need to use in-built module named as abc module.
we define abstract method(a method without body & implementation) and conceret method (normal) inside class.
we cant create object of abstract class
we need to implement the abstract method in child class 
we can define concerte method in abstract class but not abstract method in concerete class.

"""
from abc  import ABC,abstractmethod   #  (abstract base class) abc is file

class student(ABC):
     #class body 
     @abstractmethod                 
     def check_params(self):
         pass

class boy(student):
    def check_params(self):
        print("ABC")
b=boy()
b.check_params()  