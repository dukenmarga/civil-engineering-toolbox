from src import view
from model.material import concrete
from model.structure import concrete_slab
import cherrypy

class Concrete:
    def index(self):
        pass

    def flexural_analysis(self, **var):
        # Prepare view & model object
        template = view.lookup.get_template('structure/concrete_flexural_analysis.mako')
        model = concrete.Concrete()

        # Prepare url params & cookie as default value
        param = cherrypy.request.params
        cookie = cherrypy.request.cookie

        # Get url parameter or set default variable (if None)
        fyr = float(param.get('fyr') or cookie['fyr'].value)
        fc = float(param.get('fc') or cookie['fc'].value)
        height = float(param.get('height') or 565)
        width = float(param.get('width') or 250)
        n = int(param.get('n') or 4)
        diameter = float(param.get('diameter') or 13)
        cover = float(param.get('cover') or 65)

        # Calculate
        mn = model.Mn(fyr, fc, height, width, n, diameter, cover)
        rho = model.rho(n, diameter, width, height)
        rho_max = model.rho_max(fc, fyr)
        As = model.As(n, diameter)
        As_max = model.As_max(fc, fyr, height, width)
        As_min = model.As_min(fc, fyr, height, width, cover)
        eps_s = model.eps_s(height-cover, As, fc, fyr, width)
        phi = model.phi(eps_s)

        # Prepare data to view
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

    def slab_two_ways_design(self, **var):
        # Prepare view & model object
        template = view.lookup.get_template('structure/concrete_slab.mako')
        model = concrete_slab.Slab()

        # Prepare url params & cookie as default value
        param = cherrypy.request.params
        cookie = cherrypy.request.cookie

        # Get url parameter or set default variable (if None)
        ly = float(param.get('ly') or 4)
        lx = float(param.get('lx') or 3)
        t = float(param.get('t') or 0.12)
        dl = float(param.get('dl') or 100)
        ll = float(param.get('ll') or 250)
        include_self_weight = param.get('include_self_weight') or 'Yes'
        kdl = float(param.get('kdl') or 1.2)
        kll = float(param.get('kll') or 1.6)
        conc_unit_weight = float(param.get('conc_unit_weight') or cookie['conc_unit_weight'].value)
        fc = float(param.get('fc') or cookie['fc'].value)
        fus = float(param.get('fus') or cookie['fus'].value)
        slab_type = param.get('slab_type') or '1'
        diameter = float(param.get('diameter') or 10)
        dy= float(param.get('dy') or 40)
        dx= float(param.get('dx') or 50)

        # Calculate
        Mlx, Mly, Mtx, Mty, slx, sly, stx, sty, error = model.marcus_method(
                ly, lx, t, dl, ll, include_self_weight, kdl, kll,
                conc_unit_weight, fc, fus, slab_type, diameter, dy, dx)

        # Prepare data to view
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
