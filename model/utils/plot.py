import matplotlib
matplotlib.use('Agg')

from matplotlib import pyplot

import cherrypy
from cStringIO import StringIO

class Plot:
    """ Generate additional horizontal load due to
        surcharge load (e.g. Point load,
        line load, uniform load, etc)
    """
    def __init__(self):
        pass

    def image(self, x, y, z, plot_name="image.png"):
        img = StringIO()
        pyplot.pcolor(x, y, z)
        pyplot.colorbar(orientation="horizontal")

        pyplot.savefig(img, format='png')
        img.seek(0)
        pyplot.clf()
        return cherrypy.lib.static.serve_fileobj(img,
            content_type="png",
            name=plot_name)