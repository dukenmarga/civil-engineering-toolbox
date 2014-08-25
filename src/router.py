import cherrypy
from controller.structure import steel_profile
from controller.math import converter
from controller.about import about

def setup():
    #Router handler
    router = cherrypy.dispatch.RoutesDispatcher()

    #STRUCTURE
    a = steel_profile.Steel_Profile()
    router.connect(name='structure_steel_profile', route='/structure/steel_profile',
                   controller=a, action="index")
    #MATH
    a = converter.Converter()
    router.connect(name='index_converter', route='/math/unit_converter',
                   controller=a, action="index")
    router.connect(name='distance_converter', route='/math/unit_converter/distance/',
                   controller=a, action="distance")
    router.connect(name='pressure_converter', route='/math/unit_converter/pressure/',
                   controller=a, action="pressure")
    router.connect(name='force_converter', route='/math/unit_converter/force/',
                   controller=a, action="force")
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
