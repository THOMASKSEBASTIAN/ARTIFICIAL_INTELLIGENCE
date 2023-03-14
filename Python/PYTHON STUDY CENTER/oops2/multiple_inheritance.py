class Person:
    def per1(self,name,age):
        self.name=name
        self.age=age
    def prin(self):
        print(self.name,self.age)

class Person2():
    def par2(self,name1,name2):
        self.name1=name1
        self.name2=name2
        print(self.name1,self.name2)

class Person3(Person,Person2):
    def par3(self,name3,name4):
        self.name3=name3
        self.name4=name4
        print(self.name3,self.name4)

p=Person3()
p.per1("babu",27)
p.prin()
p.par2("joy",34)
p.par3("joy",34)
