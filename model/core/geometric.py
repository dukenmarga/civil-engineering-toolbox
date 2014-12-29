import math
import numpy as np
class Geometric:
    def __init__(self):
        pass
    def area(self):
        """ Calculate area of closed section
        """
        pass
    def Ixx(self, coordinate):
        """ Calculate second moment of inertia about x
        """
        inertia = 0
        n = len(coordinate)
        for i, (x, y) in enumerate(coordinate):
            if i == n-1:
                p = 0
            else:
                p = i+1
            a = x*coordinate[p][1] - coordinate[p][0]*y
            inertia = inertia + (y**2 + y*coordinate[p][1] + coordinate[p][1]**2)*a
        return float(abs(inertia/12.))
    def Iyy(self, coordinate):
        """ Calculate second moment of inertia about y
        """
        inertia = 0
        n = len(coordinate)
        for i, (x, y) in enumerate(coordinate):
            if i == n-1:
                p = 0
            else:
                p = i+1
            a = x*coordinate[p][1] - coordinate[p][0]*y
            inertia = inertia + (x**2 + x*coordinate[p][0] + coordinate[p][0]**2)*a
        return float(inertia/12.)
