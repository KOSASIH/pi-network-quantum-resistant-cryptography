import unittest

def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    for name in tests:
        if name.startswith('test_'):
            module = __import__(__name__ + '.' + name, fromlist=[name])
            tests = loader.loadTestsFromModule(module)
            suite.addTests(tests)
    return suite
