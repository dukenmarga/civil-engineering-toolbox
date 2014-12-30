from src import view
from model.geotechnic import surcharge_load
from model.utils import plot

class Surcharge_Load:
    def __init__(self):
        pass
    def point(self, q=200, x_load=1.2, H=12, start=-10, end=10, type=2):
        template = view.lookup.get_template('geotechnic/surcharge_point.mako')
        data = {
            'q': q,
            'x_load': x_load, #m
            'H': H, #m
            'start': start, #m
            'end': end, # m
            'type': type,
            'plot_image': self.point_image(q, x_load, H, start, end, type),
        }
        return template.render(**data)
    def point_image(self, q=200, x_load=1.2, H=12, start=-10, end=10, type=2):
        model = surcharge_load.Surcharge_Load()
        x, y, z = model.point(float(q), float(x_load), float(H), float(start),
                              float(end), float(type))
        plt = plot.Plot()
        return plt.pcolor(x, y, z)

    def strip(self, q=200, x_load=1.2, width=1, H=5, start=-10, end=10, type=2):
        template = view.lookup.get_template('geotechnic/surcharge_strip.mako')
        data = {
            'q': q,
            'x_load': x_load, #m
            'width': width, #m
            'H': H, #m
            'start': start, #m
            'end': end, # m
            'type': type,
            'plot_image': self.strip_image(q, x_load, width, H, start, end,
                                           type),
        }
        return template.render(**data)
    def strip_image(self, q=200, x_load=1.2, width=1, H=5, start=-10, end=10,
                    type=2):
        model = surcharge_load.Surcharge_Load()
        x, y, z = model.strip(float(q), float(x_load), float(width), float(H),
                              float(start), float(end), float(type))
        plt = plot.Plot()
        return plt.pcolor(x, y, z)
