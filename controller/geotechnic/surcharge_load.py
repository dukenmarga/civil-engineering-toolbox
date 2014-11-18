from src import view
from model.geotechnic import surcharge_load
from model.utils import plot
from doc.geotechnic import surcharge_load_doc

class Surcharge_Load:
    def __init__(self):
        pass
    def point(self, q=200, x_load=1.2, H=12, start=-10, end=10):
        template = view.lookup.get_template('geotechnic/surcharge_point.mako')
        doc = surcharge_load_doc.Surcharge_Load()
        data = {
            'q': q,
            'x_load': x_load, #m
            'H': H, #m
            'start': start, #m
            'end': end, # m
            'plot_image': self.point_image(q, x_load, H, start, end),
            'doc' : doc.point()
        }
        return template.render(**data)
    def point_image(self, q=200, x_load=1.2, H=12, start=-10, end=10):
        model = surcharge_load.Surcharge_Load()
        x, y, z = model.point(float(q), float(x_load), float(H), float(start), float(end))
        plt = plot.Plot()
        return plt.pcolor(x, y, z)

    def strip(self, q=200, x_load=1.2, width=1, H=5, start=-10, end=10):
        template = view.lookup.get_template('geotechnic/surcharge_strip.mako')

        data = {
            'q': q,
            'x_load': x_load, #m
            'width': width, #m
            'H': H, #m
            'start': start, #m
            'end': end, # m
            'plot_image': self.strip_image(q, x_load, width, H, start, end)
        }
        return template.render(**data)
    def strip_image(self, q=200, x_load=1.2, width=1, H=5, start=-10, end=10):
        model = surcharge_load.Surcharge_Load()
        x, y, z = model.strip(float(q), float(x_load), float(width), float(H), float(start), float(end))
        plt = plot.Plot()
        return plt.pcolor(x, y, z)
