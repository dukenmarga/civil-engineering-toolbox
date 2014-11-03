class Converter:
    """ Unit converter
    """
    def __init__(self):
        self.distance_unit = {
            'meter (m)': 1,
            'exameter (Em)': 1e-18,
            'petameter (Pm)': 1e-15,
            'terameter (Tm)': 1e-12,
            'gigameter (Gm)': 0.000010001,
            'megameter (Mm)': 0.000001,
            'kilometer (km)': 0.001,
            'hectometer (hm)': 0.01,
            'dekameter (dam)': 0.1,
            'decimeter (dm)': 10,
            'centimeter (cm)': 100,
            'millimeter (mm)': 1000,
            'micrometer': 1000000,
            'micron': 1000000,
            'attometer (am)': 1e+18,
            'megaparsec (Mpc)': 3.24077929e-23,
            'kiloparsec (Kpc)': 3.24077929e-20,
            'parsec (pc)': 3.24077929e-17,
            'mile (Intl)': 0.000621371,
            'mile (US survey)': 0.000621371,
            'yard': 1.093613298,
            'foot': 3.280839895,
            'feet': 3.280839895,
            'inch (in)': 39.37007874,
        }
        self.force_unit = {
            'newton (N)': 9.80665,
            'exanewton (EN)': 9.80665e-18,
            'petanewton (PN)': 9.80665e-15,
            'teranewton (TN)': 9.80665e-12,
            'giganewton (GN)': 0.00000001,
            'meganewton (MN)': 0.000009807,
            'kilonewton (kN)': 0.00980665,
            'hectonewton (hN)': 0.0980665,
            'dekanewton (daN)': 0.980665,
            'decinewton (dN)': 98.0665,
            'centinewton (cN)': 980.665,
            'milinewton (mN)': 9806.65,
            'dyne (dyn)': 980665,
            'joule/meter (J/m)': 9.80665,
            'joule/centimeter (J/cm)': 980.665,
            'gram-force (gf)': 1000,
            'kilogram-force (kgf)': 1,
            'ton-force short': 0.001102311,
            'ton-force long': 0.000984207,
            'ton-force metric (tf)': 0.001,
            'kip-force (kipf)': 0.002204623,
            'kilopound-force (kipf)': 0.002204623,
            'pound-force (lbf)': 2.204622622,
            'ounce-force (lbf)': 35.27396195,
            'poundal (pdl)': 70.931635284,
            'pound foot/square second': 70.931635284,
            'pond (p)': 1000,
            'kpond (kp)': 1,
        }
        self.pressure_unit = {
            'pascal (Pa)': 1000000,
            'exapascal (EPa)': 1e-12,
            'petapascal (PPa)': 0.000000001,
            'terapascal (TPa)': 0.000001,
            'gigapascal (GPa)': 00.001  ,
            'megapascal (MPa)': 1,
            'kilopascal (kPa)': 1000,
            'hectopascal (hPa)': 10000,
            'dekapascal (dPa)': 100000,

            'newton/m2 (N/m2)': 1000000,
            'newton/cm2 (N/cm2)': 100,
            'newton/mm2 (N/mm2)': 1,
            'kilonewton/m2 (KN/m2)': 1000,
            'bar': 10,
            'milibar': 10000,

            'kilogram-force/mm2 (kgf/mm2)': 0.101971621,
            'Standard atmoshpere (Atm)': 9.869232667,
            'kilogram/cm2 (kg/cm2)': 10.19716213,
            'kilogram/m2 (kg/m2)': 101971.62129779,

            'ksi': 0.145037738,
            'psi': 145.03773773,
        }

    def index(self):
        pass

    def convert(self, val, from_, to):
        data = float(val) * to / from_
        return data

    def distance(self, val=1, from_='m', to='micron'):
        """ Converter for distance unit
        """
        try:
            from_ = float(self.distance_unit[from_])
            to = float(self.distance_unit[to])
            data = self.convert(val, from_, to)
        except:
            return "Uups, check the number and unit!"
        return str(data)

    def force(self, val=1, from_='kgf', to='kgf'):
        """ Converter for force unit
        """
        try:
            from_ = float(self.force_unit[from_])
            to = float(self.force_unit[to])
            data = self.convert(val, from_, to)
        except:
            return "Uups, check the number and unit!"
        return str(data)

    def pressure(self, val=1, from_='pa', to='pa'):
        """ Converter for pressure unit
        """
        try:
            from_ = float(self.pressure_unit[from_])
            to = float(self.pressure_unit[to])
            data = self.convert(val, from_, to)
        except:
            return "Uups, check the number and unit!"
        return str(data)