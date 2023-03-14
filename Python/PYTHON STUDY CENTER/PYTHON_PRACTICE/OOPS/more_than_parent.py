class College():
    def __init__(self,class_name,department):
        self.class_name=class_name
        self.department=department

class Class():
    def __init__(self,class_dept_name,another_department):
        self.class_dept_name=class_dept_name
        self.another_department=another_department


class Place(College,Class):
    def __init__(self,place,code,class_name,department,class_dept_name,another_department):
        College.__init__(self,class_name,department)
        Class.__init__(self,class_dept_name, another_department)
        self.place=place
        self.code=code
    def print(self):
        print(self.place,self.code,self.class_name,self.department, self.class_dept_name,self.another_department)

p=Place("pattazhi","43","class6","ece","eee","ewe")
p.print()