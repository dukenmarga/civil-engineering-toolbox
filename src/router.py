import cherrypy
from controller.structure import steel_profile

def setup():
    #Router handler
    router = cherrypy.dispatch.RoutesDispatcher()

    #STRUCTURE
    a = steel_profile.Steel_Profile()
    router.connect(name='strct_steel_profile', route='/structure/steel_profile',
                   controller=a, action="index")

    #Connect router handler as src
    router_config = {
        "/" : {
            "request.dispatch" : router
        }
    }
    return router_config
