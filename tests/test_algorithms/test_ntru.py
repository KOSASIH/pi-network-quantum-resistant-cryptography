import unittest

from .test_ntru import NTRUTestCase
from .test_frodo import FRODOTestCase

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(NTRUTestCase))
    suite.addTests(unittest.makeSuite(FRODOTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
