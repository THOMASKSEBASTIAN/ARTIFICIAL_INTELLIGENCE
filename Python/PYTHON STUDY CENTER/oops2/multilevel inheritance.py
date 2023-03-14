class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child(Person):
    def __init__(self,school,place,name,age):
        super().__init__(name,age)
        self.school=school
        self.place=place
        print(self.school,self.place)
class Student(Child):
    def __init__(self,rollno,department,name,age,school,place):
        super().__init__(name,age,school,place)
        self.rollno=rollno
        self.department=department
        print(self.rollno,self.department)
s=Student(23,"ece","Saju",27,"oxford","TVM")



RU