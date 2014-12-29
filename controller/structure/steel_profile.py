from src import view
from model.structure import steel_profile

class Steel_Profile:
    def index(self):
        return self.iwf()
    def iwf(self):
        template = view.lookup.get_template('structure/steel_iwf_profile.mako')
        model = steel_profile.Steel_Profile()
        data = model.iwf_table()
        return template.render(**data)
    def angle(self):
        template = view.lookup.get_template('structure/steel_angle_profile.mako')
        model = steel_profile.Steel_Profile()
        data = model.angle_table()
        return template.render(**data)