from src import view
from model.options import options
import cherrypy

class About:
    def index(self):
        template = view.lookup.get_template('about/about.mako')
        return template.render()
    def license(self):
        template = view.lookup.get_template('about/license.mako')
        return template.render()
    def technology(self):
        template = view.lookup.get_template('about/technology.mako')
        return template.render()
    def home(self):
        template = view.lookup.get_template('about/home.mako')
        return template.render()
    def options(self):
        current = options.Options()
        data = current.get_options()
        template = view.lookup.get_template('about/options.mako')
        return template.render(**data)
    def set_options(self, **kwargs):
        current = options.Options()
        current.set_options(kwargs)
        raise cherrypy.HTTPRedirect("/options")
    def reset_options(self):
        current = options.Options()
        current.reset_options()
        raise cherrypy.HTTPRedirect("/options")
