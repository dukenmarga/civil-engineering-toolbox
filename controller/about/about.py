from src import view

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
        template = view.lookup.get_template('about/options.mako')
        return template.render()
