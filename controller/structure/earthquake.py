from src import view
from model.structure import earthquake
from model.utils import plot
import cherrypy

class Earthquake:
    def index(self):
        pass

    def response_spectrum(self, **var):
        # Prepare view & model object
        template = view.lookup.get_template('structure/earthquake_response_spectrum.mako')
        model = earthquake.Earthquake()

        # Prepare url params & cookie as default value
        param = cherrypy.request.params
        cookie = cherrypy.request.cookie

        # Get url parameter or set default variable (if None)
        ss = float(param.get('ss') or 1.3)
        s1 = float(param.get('s1') or 0.6)
        site_class = param.get('site_class') or "SD"

        # Calculate & get the plot image
        x, y = model.response_spectrum(ss, s1, site_class)
        plt = plot.Plot()
        img = plt.line(x, y, "Natural Period, T, (second)",
                        "Spectral Acceleration (Sa)",
                        "Response Spectrum Design")

        # Prepare data to view
        data = {
            'ss': ss,
            's1': s1, #m
            'site_class': site_class, #m
            'plot_image': img
        }

        return template.render(**data)