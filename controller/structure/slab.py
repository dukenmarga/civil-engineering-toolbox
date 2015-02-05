from src import view
from model.structure import slab

class Slab:
    def index(self):
        pass
    def two_ways(self, ly=4, lx=3, t=0.12, dl=100, ll=250,
                 include_self_weight="Yes", kdl=1.2, kll=1.6,
                 conc_unit_weight=2400, fc=25, fus=400, slab_type=1,
                 diameter=10, dy=40, dx=50):
        template = view.lookup.get_template('structure/slab.mako')
        model = slab.Slab()
        Mlx, Mly, Mtx, Mty, slx, sly, stx, sty = model.marcus_method(
                float(ly), float(lx), float(t),
                float(dl), float(ll), include_self_weight, float(kdl),
                float(kll), float(conc_unit_weight), float(fc), float(fus),
                str(slab_type), float(diameter), float(dy), float(dx))
        data = {
            'ly': ly,
            'lx': lx, #m
            't': t,
            'dl': dl,
            'll': ll,
            'include_self_weight': include_self_weight,
            'kdl': kdl,
            'kll': kll,
            'conc_unit_weight': conc_unit_weight,
            'fc': fc,
            'fus': fus,
            'slab_type': slab_type,
            'diameter': diameter,
            'dy': dy,
            'dx': dx,
            'Mlx': Mlx,
            'Mly': Mly,
            'Mtx': Mtx,
            'Mty': Mty,
            'slx': slx,
            'sly': sly,
            'stx': stx,
            'sty': sty,
        }


        return template.render(**data)
