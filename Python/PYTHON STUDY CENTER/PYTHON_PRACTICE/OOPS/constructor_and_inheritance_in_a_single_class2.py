class Vehicle():
    def __init__(self,jeep,car):
        self.jeep=jeep
        self.car=car
class Vehicle2(Vehicle):
    def __init__(self,truck,jeep,car):  super
        super().__init__(jeep,car)
        self.truck=truck
    def print(self):
        print(self.jeep,self.car,self.truck)
v=Vehicle2("mahindra","maruthi","ashok")
v.print()