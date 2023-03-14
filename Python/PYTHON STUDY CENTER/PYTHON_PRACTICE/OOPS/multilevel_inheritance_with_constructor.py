class Class():
    def __init__(self,school,dept):
        self.school = school
        self.dept = dept
class Class2(Class):
    def  __init__(self, school2,dept2):
        super().__init__(self,self.school,self.dept)
        self.school2 = school2
        self.dept2 = dept2
class Class3(Class2):
    def  __init__(self, school3,dept3):
        super().__init__(self,self.school2,self.dept3)
        self.school3 = school3
        self.dept3 = dept3


