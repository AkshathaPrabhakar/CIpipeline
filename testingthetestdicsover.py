import unittest
import json

def suite():
    loader = unittest.TestLoader()
    test_suite = loader.discover(start_dir='.', pattern='swagtest_*.py')
    return test_suite

class JSONTestResult(unittest.TextTestResult):
    def get_json(self):
        test_results = {
            'successes': [str(test) for test, _ in self.successes],
            'failures': [str(test) for test, _ in self.failures],
            'errors': [str(test) for test, _ in self.errors],
            'skipped': [str(test) for test, _ in self.skipped],
        }
        return json.dumps(test_results, indent=4)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(resultclass=JSONTestResult)
    result = runner.run(suite())
    
    # Save the results to a JSON file
    with open('test-results.json', 'w') as f:
        f.write(result.get_json())
