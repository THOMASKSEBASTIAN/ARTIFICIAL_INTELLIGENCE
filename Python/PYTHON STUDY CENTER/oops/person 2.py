class Person():
    def person1(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

    def print(self):
        print("..........")
        print(self.name,self.age,self.place)
        print("..........")

s=Person()

f = open("text.txt", "r")
for i in f:
    a=i.rstrip("\n").split(",")
    name=a[0]
    age=a[1]
    place=a[2]
    p=Person()
    p.person1(name,age,place)
    p.print()



