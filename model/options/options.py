import cherrypy
import math

class Options:
    def __init__(self):
        # Unit: MPa
        fc = 30
        self.default_options = {
            #Reinforced concrete
            'fc': fc,
            'fyr': 400,
            'Ec': '{0:.2f}'.format(4700*math.sqrt(fc)),
            'conc_unit_weight': 2400,
            #Steel structure
            'fys': 240,
            'fus': 390,
            'Es': 200000,
            'steel_unit_weight': 7850,
        }

    def set_options(self, kwargs):
        cookie = cherrypy.response.cookie
        for key, val in kwargs.iteritems():
            cookie[key] = val
            cookie[key]['max-age'] = 60*60*24*365*2  #2 years
            cookie[key]['path'] = "/"

    def get_options(self):
        cookie = cherrypy.request.cookie
        if 'fc' not in cookie:
            self.reset_options()
            raise cherrypy.HTTPRedirect("/options")
        return cookie

    def reset_options(self):
        cookie = cherrypy.response.cookie
        self.set_options(self.default_options)
        return cookie
