class Person:
    company="ABC"#static varaiable
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def prin(self):
        print(self.name,self.age,Person.company)
p=Person("babu",27)

p.prin()
