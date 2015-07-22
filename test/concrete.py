import unittest
from model.material import concrete

class Concrete(unittest.TestCase):
    '''Test concrete function from class Concrete including
    '''
    def setUp(self):
        self.c = concrete.Concrete()

    def test_Gc(self):
        '''Check shear capacity of concrete'''
        self.assertAlmostEqual(float(
            self.c.Gc(fc=20)),8757.93,
            places=2, msg="NOT OK")
        self.assertAlmostEqual(float(
            self.c.Gc(fc=20,Ec=20000)),8333.33,
            places=2, msg="NOT OK")
        self.assertAlmostEqual(float(
            self.c.Gc(fc=20,concrete_poisson_ratio=0.3)),8084.25,
            places=2, msg="NOT OK")

    def test_As(self):
        self.assertAlmostEqual(float(
            self.c.As(n=4, diameter=13)),530.93,
            places=2, msg="NOT OK")

    def test_a(self):
        self.assertAlmostEqual(float(
            self.c.a(As=530.93, fyr=420, fc=20, width=250)),52.47,
            places=2, msg="NOT OK")

    def test_jd(self):
        self.assertAlmostEqual(float(
            self.c.jd(d=500, a=52.47)),473.77,
            places=2, msg="NOT OK")

    def test_mn_under_reinforced(self):
        '''Check moment capacity under-reinforced'''
        val = {
            'fyr': 420,  #MPa
            'fc': 20,  #MPa
            'width': 250,  #mm
            'height': 565,  #mm
            'cover': 65,  #mm
            'n': 4,  #number
            'diameter': 13,  #mm
        }
        self.assertAlmostEqual(float(
            self.c.Mn(**val)),105645164.45, #N.mm
            places=2, msg="NOT OK")

    def test_beta1(self):
        self.assertAlmostEqual(float(
            self.c.beta1(fc=28)),0.85,
            places=2, msg="NOT OK")
        self.assertAlmostEqual(float(
            self.c.beta1(fc=35)),0.8,
            places=2, msg="NOT OK")
        self.assertAlmostEqual(float(
            self.c.beta1(fc=59)),0.65,
            places=2, msg="NOT OK")

    def test_rho_balance(self):
        self.assertAlmostEqual(float(
            self.c.rho_balance(fc=20, fyr=420)),0.020238,
            places=6, msg="NOT OK")
        self.assertAlmostEqual(float(
            self.c.rho_balance(fc=35, fyr=420)),0.033333,
            places=6, msg="NOT OK")
        self.assertAlmostEqual(float(
            self.c.rho_balance(fc=59, fyr=420)),0.045655,
            places=6, msg="NOT OK")

testSuite = unittest.TestSuite()
testSuite.addTest(unittest.makeSuite(Concrete))
a = unittest.TextTestRunner()
a.run(testSuite)