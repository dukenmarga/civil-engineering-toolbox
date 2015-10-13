import math

class Concrete:
    def __init__(self):
        pass

    def Gc(self, fc=None, Ec=None, concrete_poisson_ratio=0.2):
        """
        Return Estimated shear modulus
        :param fc: Concrete strength (MPa)
        :param Ec: Concrete Young modulus (MPa)
        :param concrete_poisson_ratio: Concrete Poisson's ratio
        :return: Shear modulus (MPa)
        """
        if Ec is None:
            Ec = 4700*math.sqrt(fc)
        Gc = Ec/(2*(1+concrete_poisson_ratio))  # MPa
        return Gc

    def Mn(self, fyr, fc, height, width, n, diameter, cover):
        """
        Calculate nominal moment strength of reinforced concrete
        of rectangular area
        :param fyr: Steel yield strength (MPa)
        :param fc: Concrete strength (MPa)
        :param width: Width of section (mm)
        :param height: Height of section (mm)
        :param cover: Concrete cover(mm)
        :param n: Number of tension reinforcement
        :param diameter: Diameter reinforcement (mm)
        :return: Nominal moment strength, Mn (KN)
        """

        As = self.As(n, diameter)  # mm2
        a = self.a(As, fyr, fc, width)  # mm
        d = height-cover
        jd = self.jd(d, a)
        Mn = As*fyr*jd
        return Mn

    def As(self, n, diameter):
        '''
        Calculate area of n reinforcement
        :param n: Number of reinforcement
        :param diameter: Diameter of reinforcement
        :return: Area of reinforcement
        '''
        return math.pi*diameter**2/4 * n

    def a(self, As, fyr, fc, width):
        '''
        Return equivalent height of compression (a) on concrete.
        This equivalent height is well known as Withney's stress block
        a = c*beta1
        with c      = height of compression area above neutral axis
             beta1  = coefficient, 0.85 if fc below 28 MPa
        This function calculates value of (a) using force equilibrium.
        :param As: Area of tensile reinforcement
        :param fyr: Reinforcement tensile strength
        :param fc: Concrete compressive strength
        :param width: Width of rectangular area
        :return: Equivalent height of compression on concrete
        '''
        A = As*fyr  # N
        B = 0.85*fc*width  # N/mm
        return A/B  # mm

    def jd(self, d, a):
        '''
        Return moment length, as length of center of tension force to
        center of compressive force
        :param d: Distance from center of tensile reinforcement to the further
        compressive concrete
        :param a: equivalent height of compression on concrete
        :return: moment length
        '''
        return d-a/2

    def beta1(self, fc):
        '''
        Return value of coefficient that define equivalent height of Whitney's
        stress block.
        :param fc: Concrete compressive strength
        :return: beta1
        '''
        if fc <= 28:
            return 0.85
        elif fc <= 56:
            return 0.85 - 0.05*(fc-28)/7
        else:
            return 0.65

    def rho_balance(self, fc, fyr):
        '''
        Return ratio of tension reinforcement to concrete area
        when balance condition occur. Balance condition is when
        tension reinforcement reach yield strain exactly when compression
        concrete reach ultimate strain.
        :param fc: Concrete compressive strength
        :param fyr: Steel yield tension strength
        :return: beta1
        '''
        beta1 = self.beta1(fc)
        return 0.85*beta1*fc/fyr*600/(600+fyr)

    def rho(self, n, diameter, width, height):
        '''
        :param n: number of tension reinforcement
        :param diameter: reinforcement diameter
        :param width: width of concrete
        :param height: height of concrete
        :return: ratio area of reinforcement to area of concrete
        '''
        As = self.As(n, diameter)
        Ac = width*height
        return As/Ac

    def rho_max(self, fc, fyr):
        '''
        :param fc: concrete compressive strength
        :param fyr: reinforcement yield strength
        :return: Allowable ratio area of reinforcement to area of concrete
        '''
        return 0.75*self.rho_balance(fc, fyr)

    def As_max(self, fc, fyr, height, width):
        return self.rho_max(fc, fyr) * height * width

    def As_min(self, fc, fyr, height, width, cover):
        As_min1 = 0.25*math.sqrt(fc)/fyr*(height-cover)*width
        As_min2 = 1.4/fyr*(height-cover)*width
        return max(As_min1, As_min2)

    def eps_s(self, d, As, fc, fyr, width, eps_cu=0.003):
        '''
        :param d: Distance from center of tensile reinforcement to the further
        compressive concrete
        :param c: Distance neutral axis measured from most extreme compressive
        edge to neutral axis
        :param eps_cu: Concrete ultimate strain (default=0.003)
        :return: Tensile reinforcement strain
        '''
        neutral_axis = self.neutral_axis_balance2(As, fyr, fc, width)
        return (d-neutral_axis)/neutral_axis*eps_cu

    def neutral_axis_balance(self, eps_cu, eps_y, d):
        return (eps_cu)/(eps_cu + eps_y)*d

    def neutral_axis_balance2(self, As, fyr, fc, width):
        return self.a(As, fyr, fc, width) / self.beta1(fc)

    def phi(self, eps_s):
        if eps_s >= 0.005:
            return 0.9
        elif eps_s <=0.002:
            return 0.7
        else:
            return 0.65 + (eps_s-0.002)*250/3

    def Vc(self, fc, concrete_type, height, width, cover, P):
        if P>=0:
            k = (1+P/(14*width*height))
        else:
            k = (1+0.29*P/(width*height))
        d = height-cover
        return math.sqrt(fc)*width*d*concrete_type*k/6

    def Vs(self, fyr, height, diameter, space, cover, leg):
        d = height-cover
        Av = math.pi*diameter**2/4*leg
        if space == 0 or space == -1:
            return 0
        return Av*fyr*d/space

    def shear_space(self, Vu, Vc, fyr, fc, height, width, diameter, cover, leg,
                    structure_type, slab_thickness):
        d = height-cover
        phi = 0.75
        Av = math.pi*diameter**2/4*leg
        skip_min_shear = False

        if structure_type == 1:
            if height <= 250:
                skip_min_shear = True
        elif structure_type == 2:
            if (height <= 2.5*slab_thickness or
                height <= 0.5*width) and \
                height <= 610:
                skip_min_shear = True
        else:
            skip_min_shear = True


        if phi*Vc/2 >= Vu:
            s = 0
            zone = "Zone 1, No need shear reinforcement"
        elif phi*Vc >= Vu and skip_min_shear: #Skip if footing
            s = 0
            zone = "Zone 1, No need shear reinforcement"
        elif phi*Vc >= Vu:
            s1 = 2.85*fyr/width*Av
            s2 = 16*fyr/(width*math.sqrt(fc))*Av
            s3 = d/2
            s4 = 600
            s = min(s1, s2, s3, s4)
            zone = "Zone 2, Minimum shear reinforcement."
        elif Vu <= phi*Vc + 0.33*math.sqrt(fc)*width*d:
            Av = math.pi*diameter**2/4*leg
            s1 = Av*fyr*d/(Vu/phi-Vc)
            s2 = d/2
            s3 = 600
            s = min(s1, s2, s3)
            zone = "Zone 3, Dense shear reinforcement."
        elif Vu <= phi*Vc + 0.66*math.sqrt(fc)*width*d:
            s1 = Av*fyr*d/(Vu/phi-Vc)
            s2 = d/2
            s3 = 300
            s = min(s1, s2, s3)
            zone = "Zone 4, Denser shear reinforcement."
        else:
            s = -1
            zone = "Zone 5, Profile is too small. Enlarge the section!"
        return phi, s, zone