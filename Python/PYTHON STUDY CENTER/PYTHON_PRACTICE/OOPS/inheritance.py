class A:
    def print_a(self):
        print("inside")

class B():
    def print_b(self):
        print("inside b")

class C(A,B):
    def print_c(self):
        print("inside c")

c=C()
c.print_c()
c.print_b()
c.print_a()