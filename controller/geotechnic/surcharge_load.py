from src import view
from model.geotechnic import surcharge_load
from model.utils import plot

class Surcharge_Load:
    def __init__(self):
        pass
    def point(self, q=200, x_load=1.2, H=12, start=-10, end=10):
        template = view.lookup.get_template('geotechnic/surcharge_point.mako')

        data = {
            'q': q,
            'x_load': x_load, #m
            'H': H, #m
            'start': start, #m
            'end': end, # m
            'plot_name': 'point_image.png?q='+str(q)+"&x_load="+str(x_load)+
                         "&H="+str(H)+"&start="+str(start)+"&end="+str(end)
        }
        return template.render(**data)
    def point_image_png(self, q=200, x_load=1.2, H=12, start=-10, end=10):
        model = surcharge_load.Surcharge_Load()
        x, y, z = model.point(float(q), float(x_load), float(H), float(start), float(end))
        plt = plot.Plot()
        return plt.image(x, y, z, "point_image_png")

    def strip(self, q=200, x_load=1.2, width=1, H=5, start=-10, end=10):
        template = view.lookup.get_template('geotechnic/surcharge_strip.mako')

        data = {
            'q': q,
            'x_load': x_load, #m
            'width': width, #m
            'H': H, #m
            'start': start, #m
            'end': end, # m
        }
        return template.render(**data)