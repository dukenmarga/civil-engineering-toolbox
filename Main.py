import cherrypy
import src.config as config
import src.router as router


def start():
    if __name__ == '__main__':
        global_config = config.setup()
        router_config = router.setup()

        #Append all configurations
        cherrypy.config.update(global_config)
        global_config.update(router_config)
        cherrypy.tree.mount(None, config=global_config)

        cherrypy.engine.start()
        cherrypy.engine.block()

    else:
        print
        '''Usage:
            $ python Main.py
        '''

start()
