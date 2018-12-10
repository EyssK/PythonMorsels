
from math import pi

class Circle:

    def __init__(self, a=1):
        self.radius = a

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, a):
        if a>=0:
            self.__radius = a
            self.__diameter = a*2
            self.__area = pi * self.radius * self.radius
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def diameter(self):
        return self.__diameter
    
    @diameter.setter
    def diameter(self,d):
        if d>=0:
            if type(d/2) == int:
                self.__radius = int(d/2)
            else:
                self.__radius = d/2
            self.__diameter = d
            self.__area = pi * self.radius * self.radius
        else:
            raise ValueError("Diameter cannot be negative")

    @property
    def area(self):
        return self.__area

    def __str__(self):
        return "Circle("+str(self.radius)+")"

    def __repr__(self):
        return self.__str__()

