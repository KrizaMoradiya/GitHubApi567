import unittest

def classify_triangle(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            return "Isosceles and Right"
        else:
            return "Isosceles"
    elif a != b != c:
        return "Scalene"
    else:
        return "Not a valid triangle"

class TestClassifyTriangle(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 4), "Isosceles")

    def test_isosceles_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Isosceles and Right")

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 6), "Scalene")

    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(1, 1, 3), "Not a valid triangle")

if __name__ == "__main__":
    unittest.main()
