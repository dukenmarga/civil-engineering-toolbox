import math
import src.format as frm


class Steel_Profile:
    """ Provide steel profile and its properties
    """
    mass_weight = 7850 # kg/m3
    iwf_profiles = [
        "H-100x100x6x8x10",
        "H-125x125x6.5x9x10",
        "H-150x75x5x7x8",
        "H-150x150x7x10x11",
        "H-200x100x5.5x8x11",
        "H-200x200x8x12x13",
        "H-250x125x6x9x12",
        "H-250x250x9x14x16",
        "H-300x150x6.5x9x13",
        "H-300x300x10x15x18",
        "H-350x175x7x11x14",
        "H-350x350x12x19x20",
        "H-400x200x8x13x16",
        "H-400x400x13x21x22",
        "H-450x200x9x14x18",
        "H-500x200x10x16x20",
        "H-600x200x11x17x22",
        "H-700x300x13x24x28",
        "H-800x300x14x26x28",
        "H-900x300x16x28x28",
    ]
    angle_profiles = [
        "L-25x25x3x4x2",
    ]
    fy = 2400
    rho = 7200 # kg/m3

    def __init__(self):
        pass
    def iwf_table(self):
        """ Generate and return steel profile table for H-beam (IWF)
        """
        data = {
            'geometricProperties': []
        }

        for profile in self.iwf_profiles:
            split1 = profile[2:]
            dim = split1.split('x')

            # unit mm
            h = float(dim[0])
            tw = float(dim[2])
            tf = float(dim[3])
            h1 = h-2*tf
            b = float(dim[1])
            r = float(dim[4])

            # Calculate
            A = (2*b*tf + tw*h1 + (2*r)**2 - math.pi*r**2 )/100 #cm2
            Ixx = (h1**3*tw/12. + 2*(tf**3*b/12. + tf*b*(h1+tf)**2/4.) )/10000 #cm4
            Iyy = (tw**3*h1/12 + 2*(b**3*tf/12))/10000 #cm4
            unit_weight = A/10000 * self.mass_weight #kg/m
            ix = math.sqrt(Ixx/A)
            iy = math.sqrt(Iyy/A)
            Sx = (Ixx/(h/2/10))
            Sy = (Iyy/(b/2/10))

            # Display format
            A = float('{0:.2f}'.format(A))
            unit_weight = float('{0:.2f}'.format(unit_weight))
            Ixx = float('{0:.2f}'.format(Ixx))
            Iyy = float('{0:.2f}'.format(Iyy))
            ix = float('{0:.2f}'.format(ix))
            iy = float('{0:.2f}'.format(iy))
            Sx = float('{0:.2f}'.format(Sx))
            Sy = float('{0:.2f}'.format(Sy))

            data['geometricProperties'].append([profile, tw, tf, r, A,
                                                unit_weight, Ixx, Iyy,
                                                Sx, Sy, ix, iy])
        return data
    def iwf_table(self):
        """ Generate and return steel profile table for H-beam (IWF)
        """
        data = {
            'geometricProperties': []
        }

        for profile in self.iwf_profiles:
            split1 = profile[2:]
            dim = split1.split('x')

            # unit mm
            h = float(dim[0])
            b = float(dim[1])
            b1 = b-t
            t = float(dim[2])
            r1 = float(dim[3])
            r2 = float(dim[4])

            # Calculate
            A1 = h*t - r2**2*(1-math.pi/4) #mm2
            A2 = (b1*t - r2**2*(1-math.pi/4)) #mm2
            A3 = r1**2 * (1-math.pi/4) #mm2
            A = (A1+A2+A3)/100 #cm2
            
            Ax = b1*t*(t+b1/2) + h*t**2/2 #mm3
            Ay = b1*t*(t/2) + t*h**2/2 #mm3
            cx = Ax/A #mm
            cy = Ay/A #mm
            Ixx = (cx*)/10000 #cm4
            Iyy = (tw**3*h1/12 + 2*(b**3*tf/12))/10000 #cm4
            unit_weight = A/10000 * self.mass_weight #kg/m
            ix = math.sqrt(Ixx/A)
            iy = math.sqrt(Iyy/A)
            Sx = (Ixx/(h/2/10))
            Sy = (Iyy/(b/2/10))

            # Display format
            A = float('{0:.2f}'.format(A))
            unit_weight = float('{0:.2f}'.format(unit_weight))
            Ixx = float('{0:.2f}'.format(Ixx))
            Iyy = float('{0:.2f}'.format(Iyy))
            ix = float('{0:.2f}'.format(ix))
            iy = float('{0:.2f}'.format(iy))
            Sx = float('{0:.2f}'.format(Sx))
            Sy = float('{0:.2f}'.format(Sy))

            data['geometricProperties'].append([profile, tw, tf, r, A,
                                                unit_weight, Ixx, Iyy,
                                                Sx, Sy, ix, iy])
        return data