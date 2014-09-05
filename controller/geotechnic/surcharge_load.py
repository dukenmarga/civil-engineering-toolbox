from src import view
from model.geotechnic import surcharge_load

class Surcharge_Load:
    def __init__(self):
        pass
    def point(self, q=200, x_load=1.2, H=12, start=-10, end=10):
        template = view.lookup.get_template('geotechnic/surcharge_point.mako')
        model = surcharge_load.Surcharge_Load()

        data = {
            'q': q,
            'x_load': x_load, #m
            'H': H, #m
            'start': start, #m
            'end': end, # m
        }

        return template.render(**data)