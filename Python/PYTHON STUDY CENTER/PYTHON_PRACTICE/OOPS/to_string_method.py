class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.place)
    def __str__(self):  #to string
        return (self.place+" ,  "+  self.name)
pe=Person("Thomas",34,"KTR")
print(pe)
pe2=Person("Saju",45,"Punalur")
print(pe2)