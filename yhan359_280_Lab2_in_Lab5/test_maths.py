import unittest     # Import the Python unit testing framework
import maths        # Our code to test

class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        add_results = maths.add(5,5)
        self.assertEqual(10, add_results, "Add failed")

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        fibonacci_test = maths.fibonacci(5)
        self.assertEqual(5, fibonacci_test, "Test failed")

    def test_convert_base(self):
        ''' Tests the convert base function. '''
        convert_base_test = maths.convert_base(10, 2)
        self.assertEqual('1010', convert_base_test, "Test failed")
        convert_base_test2 = maths.convert_base(10, 16)
        self.assertEqual('A', convert_base_test2, "Test failed")
   
    def test_add2(self):
        convert_base_add = maths.add(5,5,16)
        self.assertEqual('A', convert_base_add, "Test failed")
        convert_base_add2 = maths.add(5,5,2)
        self.assertEqual('1010', convert_base_add2, "Test failed")
        
    def test_factorial(self):
        f = maths.factorial(5)
        self.assertEqual(f, 120, "Test failed")

# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
