
import unittest

def classify_triangle(a, b, c):
    # Check if the input values form a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a valid triangle"

    # Check for equilateral triangle
    if a == b == c:
        return "Equilateral"

    # Check for isosceles triangle
    if a == b or b == c or a == c:
        # Check for right isosceles triangle
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Isosceles and Right"
        else:
            return "Isosceles"

    # Check for scalene triangle
    if a != b and b != c and a != c:
        # Check for right scalene triangle
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Scalene and Right"
        else:
            return "Scalene"

# Automated tests using unittest
class TestClassifyTriangle(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral")

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 7), "Isosceles")

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 6), "Scalene")

    def test_scalene_right_triangle(self):
        self.assertEqual(classify_triangle(5, 12, 13), "Scalene and Right")

    def test_not_a_valid_triangle(self):
        self.assertEqual(classify_triangle(1, 1, 2), "Not a valid triangle")

if __name__ == "__main__":
    unittest.main()
