import matplotlib
matplotlib.use('Agg')

from matplotlib import pyplot

import cherrypy
from cStringIO import StringIO
import base64

class Plot:
    """ Generate additional horizontal load due to
        surcharge load (e.g. Point load,
        line load, uniform load, etc)
    """
    def __init__(self):
        pass

    def pcolor(self, x, y, z):
        img = StringIO()
        pyplot.pcolor(x, y, z)
        pyplot.colorbar(orientation="horizontal")

        pyplot.savefig(img, format='png')
        pyplot.clf()
        return base64.encodestring(img.getvalue())