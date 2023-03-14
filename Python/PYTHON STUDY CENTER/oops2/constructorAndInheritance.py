class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("self.name,self.age")
class Person2(Person):
    def __init__(self,name1,age1):
        self.name1=name1
        self.age1=age1
        print(self.name1,self.name2)