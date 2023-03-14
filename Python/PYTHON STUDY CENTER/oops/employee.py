class Employee:
    def emp(self,name,id,designation,salary,company):
        self.name=name

        self.name = name
        self.id = id
        self.designation = designation
        self.salary = salary
        self.company = company

    def prin(self):
        print(self.name)
        print(self.id)
        print(self.designation)
        print(self.salary)
        print(self.company)
s1=Employee()
s1.emp("aju","01","senior engineer",100000,"huskey")
s1.prin()