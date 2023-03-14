  # Constructor

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def print(self):
        print(self.name,self.age,self.place)

pe=Person("anu",22,"Kollam")
pe.print()