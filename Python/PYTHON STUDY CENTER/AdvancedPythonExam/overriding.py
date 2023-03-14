#if parent and child class having same method name and same number of arguments,then the
# child class  overriding the parent class and the child class will work
class book:
    def book1(self,name,pages):
        self.name=name
        self.pages=pages
        print(self.name,self.pages)
        print("parent")
class notebook(book):
    def book1(self,nam1,pag1):
        self.nam1=nam1
        self.pag1=pag1
        print(nam1,pag1)
        print("child")
n=notebook()
n.book1("maths",102)