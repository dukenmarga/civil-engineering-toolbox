import cherrypy
from src import view
from model.structure import steel_profile

class Steel_Profile:
    @cherrypy.expose
    def index(self):
        template = view.lookup.get_template('structure/steel_profile.mako')
        model = steel_profile.Steel_Profile()
        data = model.iwf_table()

        return template.render(**data)
