class Person:
    def __init__(self,name,age,place):
        self.firstname=name
        self.age=age
        self.place = place
    def printvalue(self):
        print(self.firstname)
        print(self.age)
        print(self.place)
class Employee(Person):
    def __init__(self,id,designation,salary,company,name,age,place):
        super().__init__(name,age,place)
        self.id = id
        self.designation = designation
        self.salary = salary
        self.company = company
    def print(self):
        print(self.id,self.designation,self.salary)
s=Employee(1,"senior",10000,"icu","saju",27,"pattazhi")
s.print()
s.printvalue()
