import unittest
import math

from geometric_lib.square import area as square_area, perimeter as square_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from triangle import perimeter as triangle_perimeter, is_triangle
from geometric_lib.circle import area as circle_area, perimeter as circle_perimeter


class SquareTestCase(unittest.TestCase):

    def test_square_area(self):
        res = square_area(5)
        self.assertEqual(res, 25)

    def test_square_area_large(self):
        res = square_area(10)
        self.assertEqual(res, 100)

    def test_square_perimeter(self):
        res = square_perimeter(5)
        self.assertEqual(res, 20)

    def test_square_perimeter_large(self):
        res = square_perimeter(10)
        self.assertEqual(res, 40)


class RectangleTestCase(unittest.TestCase):

    def test_rectangle_area(self):
        res = rectangle_area(5, 6)
        self.assertEqual(res, 30)

    def test_rectangle_area_reversed(self):
        res1 = rectangle_area(5, 6)
        res2 = rectangle_area(6, 5)
        self.assertEqual(res1, res2)

    def test_rectangle_perimeter(self):
        res = rectangle_perimeter(5, 6)
        self.assertEqual(res, 22)

    def test_rectangle_perimeter_reversed(self):
        res1 = rectangle_perimeter(5, 6)
        res2 = rectangle_perimeter(6, 5)
        self.assertEqual(res1, res2)


class TriangleTestCase(unittest.TestCase):

    def test_triangle_perimeter(self):
        res = triangle_perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_triangle_perimeter_equal_sides(self):
        res = triangle_perimeter(5, 5, 5)
        self.assertEqual(res, 15)

    def test_valid_triangle(self):
        res = is_triangle(3, 4, 5)
        self.assertTrue(res)

    def test_invalid_triangle(self):
        res = is_triangle(1, 2, 5)
        self.assertFalse(res)

    def test_triangle_perimeter_equal_sides1(self):
        res = triangle_perimeter(5, 5, 5)
        self.assertEqual(res, 1)


class CircleTestCase(unittest.TestCase):

    def test_circle_area(self):
        res = circle_area(5)
        self.assertAlmostEqual(res, 25 * math.pi)

    def test_circle_area_small(self):
        res = circle_area(1)
        self.assertAlmostEqual(res, math.pi)

    def test_circle_perimeter(self):
        res = circle_perimeter(5)
        self.assertAlmostEqual(res, 10 * math.pi)

    def test_circle_perimeter_small(self):
        res = circle_perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi)
