import abc
from abc import ABC,abstractmethod
class School(ABC):
    @abstarctmethod
    def animal(self):
        pass
class Class(School):
    def class1(self,name):
        self.name=name
        print(self.name)
c=Class()
c.class1("thomas")

