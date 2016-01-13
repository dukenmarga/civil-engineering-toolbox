from src import view
from model.geotechnic import shallow_foundation
from model.utils import plot
import cherrypy

class Shallow_Foundation:
    def __init__(self):
        pass

    def analysis(self, **var):
        # Prepare view & model object
        template = view.lookup.get_template('geotechnic/shallow_foundation.mako')
        model = shallow_foundation.Shallow_Foundation()

        # Prepare url params & cookie as default value
        param = cherrypy.request.params
        cookie = cherrypy.request.cookie

        # Get url parameter or set default variable (if None)
        width = float(param.get('width') or 1)
        length = float(param.get('length') or 1)
        thick = float(param.get('thick') or 0.15)
        height = float(param.get('height') or 1.2)
        Hx = float(param.get('Hx') or 1000)
        Hy = float(param.get('Hy') or 1200)
        V = float(param.get('V') or 6000)
        qall = float(param.get('qall') or 12000)
        friction = float(param.get('friction') or 0.5)
        conc_unit_weight = float(param.get('conc_unit_weight') or cookie['conc_unit_weight'].value)

        # Calculate
        q1, q2, q3, q4, qmax, qmin, status_max, status_min, SF_slide_x,\
                SF_slide_y, SF_overturn_x, SF_overturn_y = \
                model.analysis(width, length, thick, height, Hx, Hy, V, qall, friction, conc_unit_weight)
        # Prepare data to view
        data = {
            'width': width, #m
            'length': length, #m
            'thick': thick, #m
            'height': height, #m
            'Hx': Hx, #kg
            'Hy': Hy, #kg
            'V': V, #kg
            'qall': qall, #kg/m2
            'friction': friction,
            'conc_unit_weight': conc_unit_weight, #kg/m3
            'q1': q1, #kg/m2
            'q2': q2, #kg/m2
            'q3': q3, #kg/m2
            'q4': q4, #kg/m2
            'qmax': qmax, #kg/m2
            'qmin': qmin, #kg/m2
            'status_max': status_max,
            'status_min': status_min,
            'SF_slide_x': SF_slide_x,
            'SF_slide_y': SF_slide_y,
            'SF_overturn_x': SF_overturn_x,
            'SF_overturn_y': SF_overturn_y,
        }
        return template.render(**data)