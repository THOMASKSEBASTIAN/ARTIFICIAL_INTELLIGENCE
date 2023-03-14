class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
        print(self.name)
        print(self.age)
    def __str__(self):
        return (self.name)+str(self.age)
p=Person("Thomas", 23)
print(p)