import cherrypy
import math
import model.material.geometric as geometric
from sympy import Point, Polygon


class Steel_Profile:
    """ Provide steel profile and its properties
    """
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
    unp_profiles = [
        "C-75x40x5x7x11",
    ]
    angle_profiles = [
        "L-25x25x3x4x2",
        "L-30x30x3x4x2",
        "L-40x40x3x4.5x2",
        "L-40x40x4x4.5x2",
        "L-40x40x5x4.5x3",
        "L-45x45x4x6.5x3",
        "L-45x45x5x6.5x3",
        "L-50x50x4x6.5x3",
        "L-50x50x5x6.5x3",
        "L-50x50x6x6.5x4.5",
        "L-60x60x4x6.5x3",
        "L-60x60x5x6.5x3",
        "L-60x60x6x8x4",
        "L-65x65x5x8.5x3",
        "L-65x65x6x8.5x4",
        "L-65x65x8x8.5x6",
        "L-70x70x6x8.5x4",
        "L-75x75x6x8.5x4",
        "L-75x75x9x8.5x6",
        "L-75x75x12x8.5x6",
        "L-80x80x6x8.5x4",
        "L-90x90x6x10x5",
        "L-90x90x7x10x5",
        "L-90x90x10x10x7",
        "L-90x90x13x10x7",
        "L-100x100x7x10x5",
        "L-100x100x13x10x7",
        "L-100x100x10x10x7",
        "L-120x120x8x12x5",
        "L-120x120x11x13x6.5",
        "L-120x120x12x13x6.5",
        "L-130x130x9x12x6",
        "L-130x130x15x12x8.5",
        "L-130x130x12x12x8.5",
        "L-150x150x12x14x7",
        "L-150x150x15x14x10",
        "L-150x150x19x14x10",
        "L-175x175x12x15x11",
        "L-175x175x15x15x11",
        "L-200x200x15x17x12",
        "L-200x200x20x17x12",
        "L-200x200x25x17x12",
        "L-250x250x35x24x18",
        "L-250x250x25x24x12",
    ]

    def __init__(self):
        self.data = {
            'properties': []
        }
        cookie = cherrypy.request.cookie
        self.mass_weight = float(cookie['steel_unit_weight'].value)  # kg/m3
    def iwf_table(self):
        """ Generate and return steel profile table for H-beam (IWF)
        """
        geo = geometric.Geometric()
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
            # coordinate = self.coordinate_iwf(h,b,tw,tf)
            # Ixx = geo.Ixx(coordinate)/10000 #cm4
            # Iyy = geo.Iyy(coordinate)/10000 #cm4
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

            self.data['properties'].append([profile, tw, tf, r, A,
                                                unit_weight, Ixx, Iyy,
                                                Sx, Sy, ix, iy])
        return self.data
    def coordinate_iwf(self, H, B, tw, tf):
        # Generate coordinate of points of IWF profile
        # But its still to slow using SymPy
        P = [(0,0), (B,0), (B,tf), (B/2.+tw,tf), (B/2.+tw,H-tf),
             (B,H-tf), (B,H), (0,H), (0,H-tf), (B/2.-tw, H-tf),
            (B/2.-tw, tf), (0,tf)]
        poly = Polygon(*P)
        x,y = poly.centroid.x, poly.centroid.y
        for i, e in enumerate(P):
            P[i] = (e[0]-x, e[1]-y)
        return P
    def angle_table(self):
        """ Generate and return steel profile table for angle
        """
        for profile in self.angle_profiles:
            split1 = profile[2:]
            dim = split1.split('x')

            # unit mm
            h = float(dim[0])
            b = float(dim[1])
            t = float(dim[2])
            b1 = b-t
            r1 = float(dim[3])
            r2 = float(dim[4])

            # Calculate
            A1 = h*t - r2**2*(1-math.pi/4) #mm2
            A2 = (b1*t - r2**2*(1-math.pi/4)) #mm2
            A3 = r1**2 * (1-math.pi/4) #mm2
            A = (A1+A2+A3)/100 #cm2

            Ax = b1*t*(t+b1/2) + h*t**2/2  #mm3
            Ay = b1*t*(t/2) + t*h**2/2  #mm3
            cx = Ax/(A1+A2+A3) #mm
            cy = Ay/(A1+A2+A3) #mm
            Ixx = (b1*t*(cy-t/2)**2 + t*h*(h/2-cy)**2)/10000 #cm4
            Iyy = (b*t*(b/2-cx)**2 + (h-t)*t*(cx-t/2)**2)/10000 #cm4
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

            self.data['properties'].append([profile, t, r1, r2, A,
                                                unit_weight, Ixx, Iyy,
                                                Sx, Sy, ix, iy])
        return self.data