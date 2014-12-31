import os
import src.error_404 as err

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
def setup():
    return {
        '/static' : {
            'tools.staticdir.on' : True,
            'tools.staticdir.dir': os.path.join(CURRENT_DIR, '../static'),
            'tools.staticdir.debug' : True,
            'log.screen' : True
        },
        'global' : {
            'server.socket_host' : "0.0.0.0",
            'server.socket_port' : 1234,
            'server.log_to_screen' : False,
            'server.show_tracebacks' : False,
            'autoreload.on' : False,
            'error_page.404' : err.error_404,
        },
    }
