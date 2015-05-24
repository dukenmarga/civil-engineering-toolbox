import unittest
from model.math import converter

class Math(unittest.TestCase):
    '''Test math operation from class Math including
        unit conversion
    '''
    def setUp(self):
        self.c = converter.Converter()

    # Unit Converter
    def test_m_to_m(self):
        '''Meter to meter'''
        self.assertAlmostEqual(float(
            self.c.distance(2,'meter (m)','meter (m)')),2.001,
            places=2, msg="2 m is not 2 m")
    def test_km_to_m(self):
        '''Kilometer to meter'''
        self.assertAlmostEqual(float(
            self.c.distance(2,'kilometer (km)','meter (m)')),2000.001,
            places=2, msg="2 km is not 2000 m")

testSuite = unittest.TestSuite()
testSuite.addTest(unittest.makeSuite(Math))
a = unittest.TextTestRunner()
a.run(testSuite)