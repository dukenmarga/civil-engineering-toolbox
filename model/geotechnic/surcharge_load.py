class Surcharge_Load:
    """ Generate additional vertical or horizontal load due to
        surcharge load (e.g. Point load,
        line load, uniform load, etc)
    """
    def __init__(self):
        pass

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