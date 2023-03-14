class Person:
    def per(self,name,age):
        self.name=name
        self.age=age

class Per(Person):
    def prin(self,place):
        print(self.place, self.name,self.age)
s1=Per()
s1.per("thomas",21)
s1.prin("ktr")