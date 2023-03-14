class Person:
    def per(self,name,age):
        self.name=name
        self.age=age

class Child(Person):
    def chi(self,place,school):
        self.place = place
        self.school = school

class Student(Child):
    def stu(self,rollno,department):
        self.rollno = rollno
        self.department = department
    def prin(self):
        print(self.name, self.age, self.place, self.school, self.rollno, self.department)

s=Student()
s.per("Thomas",27)
s.chi("Pattazhi","Oxford")
s.stu(27,"ECE")
s.prin()