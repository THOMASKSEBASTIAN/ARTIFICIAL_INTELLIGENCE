class A:
    def printa(self):
        print("print a")

class B:
    def printb(self):
        print("print b")

class C(A,B):
    def printc(self):
        print("print c")

c=C()
c.printc()
c.printa()
c.printb()