class Bank:
    Bankname="SBI"
    def acc_creation(self,name,accnumber):
        self.name=name
        self.accno=accnumber
        self.minimum=1000
        print(Bank.Bankname,self.name,self.accno,self.minimum)



    def deposit(self,amount):
        self.amount=amount
        self.minimum=self.minimum+self.amount
        print("Amount",self.amount,"is creadited in your bank account")
        print("Now your balance is",self.minimum)

    def withdraw(self,amount2):
        self.amount2=amount2
        if self.amount2 > self.minimum:
            print("Balance is not sufficient in your account")
        else:
            self.minimum = self.minimum - self.amount2
            print("Your account balance is",self.minimum)



ban=Bank()
ban.acc_creation("Thomas",1234)
ban.deposit(500)
ban.withdraw(500)