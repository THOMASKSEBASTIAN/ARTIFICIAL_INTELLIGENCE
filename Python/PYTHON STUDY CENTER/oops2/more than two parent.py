# wrong pgm


class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def prin(self):
        print(self.name,self.age)

class Person2():
    def __init__(self,name1,age1):
        self.name1=name1
        self.age1=age1
    def prin(self):
        print(self.name,self.age)


class Person3(Person,Person2):
    def __init__(self, name2, age2,name,age,name1,age1):
        Person.__init__(self.name,self.age)
        Person2.__init__(self.name1,self.age1)
        self.name2 = name2
        self.age2 = age2

    def prin(self):
        print(self.name, self.age)


p=Person3("babu",27)
p.

p.prin()
