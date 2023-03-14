# This puts restrictions on accessing variables and methods directly and can prevent the accidental
# modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method.
# Those types of variables are known as private variables.



class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age                      #protected file
class Person2(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        print(self.name)
        print(self.__age)
p=Person2("anu",3)

