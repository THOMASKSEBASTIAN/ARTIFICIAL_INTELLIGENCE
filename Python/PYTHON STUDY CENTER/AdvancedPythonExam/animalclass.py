class animal:
    def __init__(self,name,category):
        self.name=name
        self.category=category
        print(self.name,self.category)

class dog(animal):
    def do(self,name,caotegory):
        super().__init__(name,category)
d=dog("puppy","pomaranian")


