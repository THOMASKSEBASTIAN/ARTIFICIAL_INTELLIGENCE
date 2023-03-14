class Add():
    def num(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        sum=self.num1+self.num2
        print(sum)
s=Add()
s.num(2,3)
s.add()