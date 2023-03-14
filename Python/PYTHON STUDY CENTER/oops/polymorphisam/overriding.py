class A:
    def b(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("inside parent",self.num1+self.num2)
class B(A):
    def b(self,no1,no2):
        self.no1=no1
        self.no2=no2
        print("inside child",self.no1+self.no2)
s=B()
s.b(2,4)