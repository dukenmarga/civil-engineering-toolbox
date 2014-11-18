class Surcharge_Load:
    def __init__(self):
        pass
    def point(self):
        doc ='''According to elastic analysis by Boussinesq and later modified by Terzaghi,
additional lateral force due to point load is given by following formula.
$$For \space m <= 0.4 ; P_1 =  \\frac{0.28Q}{H^2}\\frac{n^2}{(0.16+n^2)^3} $$

$$For \space m > 0.4 ; P_1 =  \\frac{1.77Q}{H^2}\\frac{m^2n^2}{(m^2+n^2)^3} $$

For any other points on both sides of point load, additional load is smaller:

$$P_Q = P_1 \\cos^2(1.1\\psi) $$
<img width="500" src="/static/picture/geotechnic/point_load.svg"></img>
        '''
        return doc
    def strip(self):
        doc = ""
        return doc