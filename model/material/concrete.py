import model.options.options as option

class Concrete:
    def __init__(self, fc):
        self.option = option.Options()
        Ec = self.option.get_options("Ec")
        pass
    def Mn(self, fy=400, fc=28, b=300, h=500, cover=40, reinforcement=2):
        """ Calculate area of closed section
        """
        pass