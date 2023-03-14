class Person:
    def __init__(self,name,age,place):
        self.firstname=name
        self.age=age
        self.place = place
    def printvalue(self):
        print(self.firstname)
        print(self.age)
        print(self.place)
class Student(Person):
    def __init__(self,roll_number,department,college_name,name,age,place):
        super().__init__(name,age,place)
        self.roll = roll_number
        self.department = department
        self.college_name = college_name
    def print(self):

        print(self.roll,self.department,self.college_name)
s=Student(1,"ece","james","thomas",27,"pattazhi")
s.print()
s.printvalue()
