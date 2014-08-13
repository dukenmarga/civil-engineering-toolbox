import cherrypy
from controller.structure import steel_profile
from controller.about import about

def setup():
    #Router handler
    router = cherrypy.dispatch.RoutesDispatcher()

    #STRUCTURE
    a = steel_profile.Steel_Profile()
    router.connect(name='structure_steel_profile', route='/structure/steel_profile',
                   controller=a, action="index")
    #ABOUT
    a = about.About()
    router.connect(name='about', route='/about',
                   controller=a, action="index")
    router.connect(name='license', route='/about/license',
                   controller=a, action="license")
    router.connect(name='technology', route='/about/technology',
                   controller=a, action="technology")
    router.connect(name='home', route='/',
                   controller=a, action="home")


    #Connect router handler as src
    router_config = {
        "/" : {
            "request.dispatch" : router
        }
    }
    return router_config
