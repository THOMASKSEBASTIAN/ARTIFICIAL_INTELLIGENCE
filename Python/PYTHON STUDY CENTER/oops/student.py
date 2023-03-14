class Student:
    def student(self,name,roll_number,department,college_name):
        self.name=name
        self.roll = roll_number
        self.department = department
        self.college_name = college_name
    def print(self):
        print(self.name)
        print(self.roll)
        print(self.department)
        print(self.college_name)
p=Student()
# p.student("bai",27,"ece","james")
p.print()