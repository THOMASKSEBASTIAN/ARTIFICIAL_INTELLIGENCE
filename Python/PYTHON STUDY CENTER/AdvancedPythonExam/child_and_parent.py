class vehicle:
    def veh(self,name,number,model,price):
        self.name=name
        self.number=number
        self.model=model
        self.price=price
        print(self.name,self.number,self.model,self.price)
class bus(vehicle):
    def bu(self,number_of_tyres):
        self.number_of_tyres=number_of_tyres
        print(self.number_of_tyres)
c=bus()
c.bu(4)
c.veh("Santro","KL27P6030",2004,1000000)