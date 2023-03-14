# # All the classa variables are public
#
# class Car():
#     def __init__(self,windows,doors,enginetype):
#         self.windows=windows
#         self.doors=doors
#         self.enginetype=enginetype
# #
# # audi=Car(4,5,"Diesel")
# # dir(audi)
#
#
# # All the class variables are protected
#
# class Car():
#     def __init__(self,windows,doors,enginetype):
#         self._windows=windows
#         self._doors=doors
#         self._enginetype=enginetype
#
# class Truck(Car):
#     def __init__(self,windows,doors,enginetype,wheels):
#         super().__init__(windows,doors,enginetype)
#         self.wheels=wheels
#
# truck=Truck(4,5,"Diesel",6)
# dir(truck)


# Private

class Car():
    def __init__(self,windows,doors,enginetype):
        self.__windows=windows
        self.__doors=doors
        self.__enginetype=enginetype
audi=Car(4,5,"Diesel")
dir(audi)
