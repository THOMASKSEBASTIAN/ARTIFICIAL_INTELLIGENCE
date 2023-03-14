class Person:
    def person(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)


class Parent:
    def par(self,place,phno):
        self.place=place
        self.phno=phno
        print(self.place)
        print(self.phno)


class employee(Person,Parent):
    def emp(self,id,designation,salary):
        self.id=id
        self.designation=designation
        self.salary = salary
        print(self.id)
        print(self.designation)
        print(self.salary)
c=employee()
c.emp(1,"senior",30000)
c.person("Madhu",27)
c.par("Pattazhi",8156924891)