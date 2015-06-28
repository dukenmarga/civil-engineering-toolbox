import cherrypy
from controller.structure import steel_profile
from controller.structure import earthquake
from controller.structure import slab
from controller.structure import concrete
from controller.geotechnic import surcharge_load
from controller.math import converter
from controller.about import about

def setup():
    #Router handler
    router = cherrypy.dispatch.RoutesDispatcher()

    #STRUCTURE
    a = steel_profile.Steel_Profile()
    router.connect(name='structure_steel_profile', route='/structure/steel/profile',
                   controller=a, action="index")
    router.connect(name='structure_steel_profile', route='/structure/steel/profile/iwf',
                   controller=a, action="iwf")
    router.connect(name='structure_steel_profile', route='/structure/steel/profile/angle',
                   controller=a, action="angle")
    a = earthquake.Earthquake()
    router.connect(name='earthquake_response_spectrum', route='/structure/earthquake/response-spectrum',
                   controller=a, action="response_spectrum")
    a = slab.Slab()
    router.connect(name='slab', route='/structure/concrete/slab-two-ways',
                   controller=a, action="two_ways")
    a = concrete.Concrete()
    router.connect(name='flexural_analysis', route='/structure/concrete/flexural-analysis',
                   controller=a, action="flexural_analysis")
    #GEOTECHNIC
    a = surcharge_load.Surcharge_Load()
    router.connect(name='surcharge_point', route='/geotechnic/surcharge/point-load',
                   controller=a, action="point")
    router.connect(name='surcharge_strip', route='/geotechnic/surcharge/strip-load',
                   controller=a, action="strip")
    #MATH
    a = converter.Converter()
    router.connect(name='index_converter', route='/math/unit-converter',
                   controller=a, action="index")
    router.connect(name='distance_converter', route='/math/unit-converter/distance/',
                   controller=a, action="distance")
    router.connect(name='pressure_converter', route='/math/unit-converter/pressure/',
                   controller=a, action="pressure")
    router.connect(name='force_converter', route='/math/unit-converter/force/',
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
    router.connect(name='options', route='/options',
                   controller=a, action="options")
    router.connect(name='reset_options', route='/options/reset',
                   controller=a, action="reset_options")
    router.connect(name='set_options', route='/options/save',
                   controller=a, action="set_options")


    #Connect router handler as src
    router_config = {
        "/" : {
            "request.dispatch" : router
        }
    }
    return router_config
