class Person():
    company="MY EDGA"
    def set_values(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def print(self):
        print(self.name)
        print(self.age)
        print(self.place)
        print(Person.company)
pe=Person()
pe.set_values("Anju",35,"Kollam")
pe.print()