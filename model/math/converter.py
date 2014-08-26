class Converter:
    """ Unit converter
    """
    def __init__(self):
        self.distance_unit = {
            'kilometer (km)': 0.001,
            'hectometer (hm)': 0.01,
            'decameter (dam)': 0.1,
            'feet': 3.280839895,
            'foot': 3.280839895,
            'meter (m)': 1,
            'decimeter (dm)': 10,
            'centimeter (cm)': 100,
            'millimeter (mm)': 1000,
            'inch': 39.37007874,
            'mile (US survey)': 0.000621371,
            'micrometer': 1000000,
            'micron': 1000000,
        }
        self.force_unit = {
            'dyne (dyn)': 980665,
            'kilonewton (kN)': 0.00980665,
            'kilopound-force (kipf)': 0.002204623,
            'kip-force (kipf)': 0.002204623,
            'newton (N)': 9.80665,
            'pound-force (lbf)': 2.204622622,
            'kilogram-force (kgf)': 1,
            'kpond (kp)': 1,
            'pond (p)': 1000,
            'meganewton (MN)': 0.000009807,
            'ton-force (metric)': 0.001,
        }
        self.pressure_unit = {
            'kilogram-force/mm2 (kgf/mm2)': 0.101971621,
            'ksi': 0.145037738,
            'megapascal (MPa)': 1,
            'pascal (Pa)': 1000000,
            'newton/mm2 (N/mm2)': 1,
            'Standard atmoshpere (Atm)': 9.869232667,
            'psi': 145.03773773,
            'kilogram/cm2 (kg/cm2)': 10.19716213,
            'kilogram/m2 (kg/m2)': 101971.62129779,
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