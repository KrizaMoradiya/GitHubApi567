import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):

    def run_test(self, test_id, input_values, expected_result):
        result = classifyTriangle(*input_values)
        self.assertEqual(result, expected_result, f"Test {test_id} failed. Input: {input_values}, Expected: {expected_result}, Actual: {result}")

    def testEquilateralTriangle(self):
        self.run_test(1, (3, 3, 3), 'Equilateral')

    def testIsoscelesTriangle(self):
        self.run_test(2, (3, 4, 3), 'Isosceles')

    def testScaleneTriangle(self):
        self.run_test(3, (5, 6, 7), 'Scalene')

    def testRightTriangleA(self):
        self.run_test(4, (3, 4, 5), 'Right')

    def testRightTriangleB(self):
        self.run_test(5, (5, 3, 4), 'Right')

    def testNotATriangle(self):
        self.run_test(6, (1, 1, 2), 'NotATriangle')

    def testInvalidInput(self):
        self.run_test(7, (201, 100, 150), 'InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
#hiiii