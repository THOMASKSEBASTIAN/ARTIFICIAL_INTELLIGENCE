# class person:
#     def setvalue(self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place
#     def printvalues(self):
#         print(self.name)
#         print(self.age)
#         print(self.place)
# p=person()
# p.setvalue("jai",27,"kochi")
# p.printvalues()













class Person:
    place="chathanoor"
    def per(self,name,age):
        self.name=name
        self.age=age

        print(self.name,self.age,Person.place)
p=Person()
p.per("isahac",30)