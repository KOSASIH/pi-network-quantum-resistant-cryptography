import unittest

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().discover('test_keys', pattern='test*.py'))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
