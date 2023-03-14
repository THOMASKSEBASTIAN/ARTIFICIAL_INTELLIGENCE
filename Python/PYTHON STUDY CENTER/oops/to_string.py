class person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalues(self):
        print(self.name)
        print(self.age)
        print(self.place)
    def __str__(self):
        return str(self.age)+self.name
p=person()
p.setvalue("jai",27,"kochi")
print(p)
