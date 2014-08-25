from src import view
from model.math import converter

class Converter:
    def __init__(self):
        self.model = converter.Converter()
    def index(self):
        template = view.lookup.get_template('math/unit_converter.mako')
        model = converter.Converter()
        distance = ""
        pressure = ""
        force = ""
        for key, val in model.distance_unit.items():
            distance += "<option value='"+ key +"'>" + key + "</option>"
        for key, val in model.pressure_unit.items():
            pressure += "<option value='"+ key +"'>" + key + "</option>"
        for key, val in model.force_unit.items():
            force += "<option value='"+ key +"'>" + key + "</option>"
        data = {
            'distance': distance,
            'pressure': pressure,
            'force': force,
        }
        return template.render(**data)
    def distance(self, val, from_, to):
        data = self.model.distance(val, from_, to)
        return data
    def pressure(self, val, from_, to):
        data = self.model.pressure(val, from_, to)
        return data
    def force(self, val, from_, to):
        data = self.model.force(val, from_, to)
        return data
