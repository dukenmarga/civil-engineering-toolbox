import cherrypy
import model.options.options as op

def check_options_value():
    cookie = cherrypy.request.cookie
    # check only one value whether it has been assigned before
    try:
        float(cookie['conc_unit_weight'].value) == 20
    except:
        option = op.Options()
        option.reset_options()