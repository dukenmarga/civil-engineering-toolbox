class Shallow_Foundation:
    """ Shallow foundation design & analysis
    """
    def __init__(self):
        pass

    def analysis(self, width, length, t, height, Hx, Hy, V, qall, friction, conc_unit_weight):
        """ Analysis of shallow foundation
            using elastic approach
        """
        area = width*length
        Sx = width*length**2/6
        Sy = length*width**2/6

        #Load
        Mx = Hx*height
        My = Hy*height

        #Pressure
        a = V/area
        b = Mx/Sx
        c = My/Sy

        #Combination pressure
        q1 = a + b + c
        q2 = a + b - c
        q3 = a - b + c
        q4 = a - b - c

        #Cek for minimum & maximum pressure
        qmin = min(q1, q2, q3, q4)
        qmax = max(q1, q2, q3, q4)
        if qmax > qall:
            status_max = "NOT OK"
        else:
            status_max = "OK"
        if qmin < 0:
            status_min = "NOT OK"
        else:
            status_min = "OK"

        #Cek for sliding stability
        vol = area*t
        m = vol*conc_unit_weight

        slide_resist = (m+V) * friction
        SF_slide_x = slide_resist/Hx
        SF_slide_y = slide_resist/Hy

        #Cek for overturning stability
        overturn_load_x = Hx*height
        overturn_load_y = Hy*height
        overturn_resist_x = (m+V)*width/2
        overturn_resist_y = (m+V)*length/2
        SF_overturn_x = overturn_resist_x/overturn_load_x
        SF_overturn_y = overturn_resist_y/overturn_load_y


        return q1, q2, q3, q4, qmax, qmin, status_max, status_min, SF_slide_x,\
                SF_slide_y, SF_overturn_x, SF_overturn_y