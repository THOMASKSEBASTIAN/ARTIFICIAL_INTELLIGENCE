class Person:
    def __init__(self,name,age,place):
        self.firstname=name
        self.age=age
        self.place = place
    def printvalue(self):
        print(self.firstname)
        print(self.age)
        print(self.place)

class Parent:
    def __init__(self,height):
        self.height=height
    def printvalue2(self):
        print(self.height)

class Employee(Person,Parent):
    def __init__(self,id,designation,salary,company,name,age,place,height):
        Person.__init__(self,name,age,place)
        Parent.__init__(self,height)
        self.id = id
        self.designation = designation
        self.salary = salary
        self.company = company
    def print(self):
        print(self.id,self.designation,self.salary)
s=Employee(1,"senior",10000,"icu","saju",27,"pattazhi",160)
s.print()
s.printvalue()
s.printvalue2()
