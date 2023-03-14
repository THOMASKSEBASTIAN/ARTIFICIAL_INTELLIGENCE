class Student:
    def student1(self,name,rollnumber,department,mark):
        self.name=name
        self.rollnumber=rollnumber
        self.department=department
        self.mark=mark

    def print(self):
        print(self.name,self.rollnumber,self.department,self.mark)

t=open("student.txt","r")
for i in t:
    # print(i)
    a=i.rstrip("\n").split(",")
    # print(a)
    name=a[0]
    rollnumber=a[1]
    department=a[2]
    mark=a[3]
    s=Student()
    s.student1(name,rollnumber,department,mark)
    s.print()