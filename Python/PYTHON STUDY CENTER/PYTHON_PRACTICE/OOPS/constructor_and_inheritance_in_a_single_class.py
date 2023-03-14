class College():
    def __init__(self,class_name,department):
        self.class_name=class_name
        self.department=department
class Place(College):
    def __init__(self,place,code,class_name,department):
        super().__init__(class_name,department)
        self.place=place
        self.code=code
    def print(self):
        print(self.place,self.code,self.class_name,self.department)

p=Place("pattazhi","43","class6","ece")
p.print()