import unittest

def suite():
    loader = unittest.TestLoader()
    test_suite = loader.discover(start_dir='.', pattern='swagtest_*.py')
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # Run the entire suite
    result = runner.run(suite())

