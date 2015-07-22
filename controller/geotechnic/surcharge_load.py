from src import view
from model.geotechnic import surcharge_load
from model.utils import plot
import cherrypy

class Surcharge_Load:
    def __init__(self):
        pass

    def point(self, **var):
        # Prepare view & model object
        template = view.lookup.get_template('geotechnic/surcharge_point.mako')
        model = surcharge_load.Surcharge_Load()

        # Prepare url params & cookie as default value
        param = cherrypy.request.params
        cookie = cherrypy.request.cookie

        # Get url parameter or set default variable (if None)
        q = float(param.get('q') or 200)
        x_load = float(param.get('x_load') or 1.2)
        H = float(param.get('H') or 12)
        start = float(param.get('start') or -10)
        end = float(param.get('end') or 10)
        type = float(param.get('type') or 2)

        # Calculate
        x, y, z = model.point(q, x_load, H, start, end, type)
        plt = plot.Plot()
        img = plt.pcolor(x, y, z)

        # Prepare data to view
        data = {
            'q': q,
            'x_load': x_load, #m
            'H': H, #m
            'start': start, #m
            'end': end, # m
            'type': type,
            'plot_image': img,
        }
        return template.render(**data)

    def strip(self, **var):
        # Prepare view & model object
        template = view.lookup.get_template('geotechnic/surcharge_strip.mako')
        model = surcharge_load.Surcharge_Load()

        # Prepare url params & cookie as default value
        param = cherrypy.request.params
        cookie = cherrypy.request.cookie

        # Get url parameter or set default variable (if None)
        q = float(param.get('q') or 200)
        x_load = float(param.get('x_load') or 1.2)
        width = float(param.get('width') or 1)
        H = float(param.get('H') or 5)
        start = float(param.get('start') or -10)
        end = float(param.get('end') or 10)
        type = float(param.get('type') or 2)

        # Calculate
        x, y, z = model.strip(q, x_load, width, H, start, end, type)
        plt = plot.Plot()
        img = plt.pcolor(x, y, z)

        data = {
            'q': q,
            'x_load': x_load, #m
            'width': width, #m
            'H': H, #m
            'start': start, #m
            'end': end, # m
            'type': type,
            'plot_image': img
        }
        return template.render(**data)