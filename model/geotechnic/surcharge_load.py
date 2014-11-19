import math
import numpy as np
class Surcharge_Load:
    """ Generate additional horizontal load due to
        surcharge load (e.g. Point load,
        line load, uniform load, etc)
    """
    def __init__(self):
        pass

    def point(self, q, x_load, H, start, end):
        """ Point load
        """
        m = x_load/H
        if m>0.4:
            A = 1.77
            B = pow(m,2)
            C = B
        else:
            A = 0.28
            B = 0.16
            C = 1

        divider = 100

        # x is left and right distance to from load
        # y is depth of soil
        # z is additional horizontal load
        # X, Y, Z are meshgrid coordinat to plot to Matplotlib
        x = np.linspace(start, end, divider)
        y = np.linspace(0, H, divider)
        X,Y = np.meshgrid(x,y)

        Z = []
        for i in x:
            pi = math.atan2(i, x_load) #rad
            for j in y:
                n = j/H
                z = A*q/math.pow(H,2)*C*n/math.pow(B+n,3)
                z = -z*math.pow(math.cos(1.1*pi),2)
                Z.append(z)
        Z = np.array(Z).reshape((len(y), len(x))).transpose()
        return X, -Y, -Z
    def strip(self, q, x_load, width, H, start, end):
        """ Strip load
        """
        divider = 100

        # x is left and right distance to from load
        # y is depth of soil
        # z is additional horizontal load
        # X, Y, Z are meshgrid coordinat to plot to Matplotlib
        x = np.linspace(start, end, divider)
        y = np.linspace(0, H, divider)
        X,Y = np.meshgrid(x,y)

        Z = []
        for i in x:
            for j in y:
                alpha = math.atan2(x_load+width/2, j) #rad
                gamma = math.atan2(x_load+width, j) #rad
                beta = (gamma-alpha)*2 #rad

                z = 2*q/math.pi*( (beta+math.sin(beta))*pow(math.sin(alpha),2) + (beta-math.sin(alpha))*pow(math.cos(alpha),2) )
                Z.append(z)
        Z = np.array(Z).reshape((len(y), len(x))).transpose()
        return X, -Y, Z