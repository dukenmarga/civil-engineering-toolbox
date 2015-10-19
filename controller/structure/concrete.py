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

    def oneway_shear_design(self, **var):
        # Prepare view & model object
        template = view.lookup.get_template('structure/concrete_oneway_shear_design.mako')
        model = concrete.Concrete()

        # Prepare url params & cookie as default value
        param = cherrypy.request.params
        cookie = cherrypy.request.cookie

        # Get url parameter or set default variable (if None)
        fyr = float(param.get('fyr') or cookie['fyr'].value)
        fc = float(param.get('fc') or cookie['fc'].value)
        concrete_type = float(param.get('concrete_type') or 1)
        structure_type = float(param.get('structure_type') or 1)
        slab_thickness = float(param.get('slab_thickness') or 120)
        height = float(param.get('height') or 400)
        width = float(param.get('width') or 250)
        diameter = float(param.get('diameter') or 10)
        cover = float(param.get('cover') or 40)
        leg = float(param.get('leg') or 2)
        Vu = float(param.get('Vu') or 20000)
        P = float(param.get('P') or 0)

        # Calculate
        Vc = model.Vc1(fc, concrete_type, height, width, cover, P)
        phi, space, zone = model.shear_space(Vu, Vc, fyr, fc, height, width,
                                             diameter, cover, leg, structure_type,
                                             slab_thickness)
        Vs = model.Vs(fyr, height, diameter, space, cover, leg)

        # Prepare data to view
        data = {
            'fc': fc,  #MPa
            'concrete_type': concrete_type,
            'structure_type': structure_type,
            'slab_thickness': int(slab_thickness),
            'fyr': int(fyr),  #MPa
            'height': int(height),  #mm
            'width': int(width),  #mm
            'diameter': int(diameter),  #mm
            'cover': int(cover),  #mm
            'leg': int(leg),  #mm
            'P': int(P),
            'Vu': int(Vu),
            'phi': float('{0:.2f}'.format(phi)),
            'Vc': float('{0:.2f}'.format(Vc)),
            'space': int(space),
            'zone': zone,
            'Vs': int(Vs),
        }

        return template.render(**data)
    def twoway_shear_design(self, **var):
        # Prepare view & model object
        template = view.lookup.get_template('structure/concrete_twoway_shear_design.mako')
        model = concrete.Concrete()

        # Prepare url params & cookie as default value
        param = cherrypy.request.params
        cookie = cherrypy.request.cookie

        # Get url parameter or set default variable (if None)
        fyr = float(param.get('fyr') or cookie['fyr'].value)
        fc = float(param.get('fc') or cookie['fc'].value)
        concrete_type = float(param.get('concrete_type') or 1)
        column_type = float(param.get('column_type') or 40)
        thickness = float(param.get('thickness') or 120)
        perimeter = float(param.get('perimeter') or 500)
        width = float(param.get('width') or 500)
        length = float(param.get('length') or 500)
        diameter = float(param.get('diameter') or 10)
        cover = float(param.get('cover') or 40)
        leg = float(param.get('leg') or 2)
        Vu = float(param.get('Vu') or 20000)

        # Calculate
        Vc = model.Vc2(fc, concrete_type, column_type, thickness, perimeter, width, length, cover)

        # Prepare data to view
        data = {
            'fyr': int(fyr),  #MPa
            'fc': fc,  #MPa
            'concrete_type': concrete_type,
            'column_type': column_type,
            'thickness': int(thickness),
            'perimeter': int(perimeter),  #mm
            'width': int(width),  #mm
            'length': int(length),  #mm
            'diameter': int(diameter),  #mm
            'cover': int(cover),  #mm
            'leg': int(leg),  #mm
            'Vu': int(Vu),
            'phi': 0.75,
            'Vc': float('{0:.2f}'.format(Vc)),
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
