class Person:
    def per1(self,name,age):
        self.name=name
        self.age=age
    def prin(self):
        print(self.name,self.age)

class Person2(Person):
    def par2(self,name1,name2):
        self.name1=name1
        self.name2=name2
        print(self.name1,self.name2)

p=Person2()
p.per1("babu",27)
p.prin()
p.par2("joy",34)
