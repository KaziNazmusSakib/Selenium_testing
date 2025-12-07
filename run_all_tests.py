import unittest

# Discover all tests in the 'tests' folder
loader = unittest.TestLoader()
suite = loader.discover('tests', pattern='test_*.py')

# Run the tests with verbosity for detailed output
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
