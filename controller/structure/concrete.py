from src import view
from model.material import concrete
from model.structure import concrete_slab

class Concrete:
    def index(self):
        pass
    def flexural_analysis(self, fc=20, fyr=420, height=565, width=250, n=4,
                          diameter=13, cover=65):
        template = view.lookup.get_template('structure/concrete_flexural_analysis.mako')
        model = concrete.Concrete()
        val = {
            'fyr': float(fyr),  #MPa
            'fc': float(fc),  #MPa
            'width': float(width),  #mm
            'height': float(height),  #mm
            'cover': float(cover),  #mm
            'n': float(n),  #number
            'diameter': float(diameter),  #mm
        }
        mn = model.Mn(**val)
        rho = model.rho(float(n), float(diameter), float(width), float(height))
        rho_max = model.rho_max(float(fc), float(fyr))
        As = model.As(float(n), float(diameter))
        As_max = model.As_max(float(fc), float(fyr), float(height), float(width))
        As_min = model.As_min(float(fc), float(fyr), float(height), float(width),
                              float(cover))
        eps_s = model.eps_s(float(height)-float(cover), As, float(fc), float(fyr), float(width))
        phi = model.phi(eps_s)

        data = {
            'fyr': fyr,  #MPa
            'fc': fc,  #MPa
            'width': width,  #mm
            'height': height,  #mm
            'cover': cover,  #mm
            'n': n,  #number
            'diameter': diameter,  #mm
            'mn': float('{0:.2f}'.format(mn/1E6)),
            'rho': float('{0:.5f}'.format(rho)),
            'rho_max': float('{0:.5f}'.format(rho_max)),
            'As': float('{0:.2f}'.format(As)),
            'As_max': float('{0:.2f}'.format(As_max)),
            'As_min': float('{0:.2f}'.format(As_min)),
            'eps_s': float('{0:.4f}'.format(eps_s)),
            'phi': float('{0:.2f}'.format(phi)),
        }

        return template.render(**data)
    def slab_two_ways_design(self, ly=4, lx=3, t=0.12, dl=100, ll=250,
                 include_self_weight="Yes", kdl=1.2, kll=1.6,
                 conc_unit_weight=2400, fc=25, fus=400, slab_type=1,
                 diameter=10, dy=40, dx=50):
        template = view.lookup.get_template('structure/concrete_slab.mako')
        model = concrete_slab.Slab()
        Mlx, Mly, Mtx, Mty, slx, sly, stx, sty, error = model.marcus_method(
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
            'Mlx': float('{0:.2f}'.format(Mlx)),
            'Mly': float('{0:.2f}'.format(Mly)),
            'Mtx': float('{0:.2f}'.format(Mtx)),
            'Mty': float('{0:.2f}'.format(Mty)),
            'slx': int(slx),
            'sly': int(sly),
            'stx': int(stx),
            'sty': int(sty),
            'error': error,
        }


        return template.render(**data)
