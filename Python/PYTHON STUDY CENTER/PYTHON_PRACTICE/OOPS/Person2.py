class Person:
    def setvalues(self,name,age,place):
        self.firstname=name
        self.age=age
        self.place=place
    def printvalues(self):
        print(self.firstname)
        print(self.age)
        print(self.place)
pe=Person()
pe.setvalues("ann",27,"kottayam")
pe.printvalues()