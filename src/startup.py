import cherrypy
import model.options.options as op

def check_options_value():
    cookie = cherrypy.request.cookie
    try:
        float(cookie['conc_unit_weight'].value) == 20
    except:
        option = op.Options()
        option.reset_options()