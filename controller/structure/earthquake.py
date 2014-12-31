from src import view
from model.structure import earthquake
from model.utils import plot

class Earthquake:
    def index(self):
        pass
    def response_spectrum(self, ss=1.3, s1=0.6, site_class="SD"):
        template = view.lookup.get_template('structure/earthquake_response_spectrum.mako')
        data = {
            'ss': ss,
            's1': s1, #m
            'site_class': site_class, #m
            'plot_image': self.point_image(ss, s1, site_class),
        }

        return template.render(**data)
    def point_image(self, ss=1.3, s1=0.6, site_class="SD"):
        model = earthquake.Earthquake()
        x, y = model.response_spectrum(float(ss), float(s1),
                              site_class)
        plt = plot.Plot()
        return plt.line(x, y, "Structural Natural Period, T, (second)",
                        "Coefficient of Structure Acceleration (Sa)",
                        "Response Spectrum Design")
