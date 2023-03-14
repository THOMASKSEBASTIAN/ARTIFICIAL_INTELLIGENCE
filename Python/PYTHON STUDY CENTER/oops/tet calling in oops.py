class Person:
    def person1(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def print(self):
        print("..........")
        print(self.name,self.age,self.place)
        print("..........")

t=open("text.txt","r")
for  i in t:
    s=i.rstrip("\n").split(",")
    print(s)
    # name=s[0]
    # age=s[1]
    # place=s[2]
    # p=Person()
    # p.person1(name,age,place)
    #
    # p.print()