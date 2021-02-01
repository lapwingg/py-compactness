import unittest
import numpy as np
from compactness import CalculateCompactness


class MyTestCase(unittest.TestCase):
    def test_perimeter_to_area_circle(self):
        circle_r = 5.0
        circle_perimeter = 2 * np.pi * circle_r
        circle_area = np.pi * (circle_r ** 2)
        result = CalculateCompactness.perimeter_to_area(perimeter=circle_perimeter, area=circle_area)
        self.assertAlmostEqual(result, 4 * np.pi, delta=0.1)

    def test_perimeter_to_area_square(self):
        square_size = 5.0
        square_perimeter = 4 * square_size
        square_area = square_size ** 2
        result = CalculateCompactness.perimeter_to_area(perimeter=square_perimeter, area=square_area)
        self.assertAlmostEqual(result, 16.0, delta=0.1)

    def test_perimeter_to_area_examples(self):
        result = CalculateCompactness.perimeter_to_area(perimeter=62.83, area=314.15)
        self.assertAlmostEqual(result, 12.56, delta=0.1)

        result = CalculateCompactness.perimeter_to_area(perimeter=79.57, area=319.25)
        self.assertAlmostEqual(result, 19.81, delta=0.1)

        result = CalculateCompactness.perimeter_to_area(perimeter=80, area=400)
        self.assertAlmostEqual(result, 16.0, delta=0.1)

    def test_isoperimetric_ratio_circle(self):
        circle_r = 7.0
        circle_perimeter = 2 * np.pi * circle_r
        circle_area = np.pi * (circle_r ** 2)
        result = CalculateCompactness.isoperimetric_ratio(perimeter=circle_perimeter, area=circle_area)
        self.assertAlmostEqual(result, 1.0, delta=0.1)

    def test_isoperimetric_ratio_square(self):
        square_size = 6.0
        square_perimeter = 4 * square_size
        square_area = square_size ** 2
        result = CalculateCompactness.isoperimetric_ratio(perimeter=square_perimeter, area=square_area)
        self.assertAlmostEqual(result, np.pi / 4, delta=0.1)

    def test_digital_compactness_circle(self):
        circle_r = 7.0
        circle_area = np.pi * (circle_r ** 2)
        minimal_circle_area = circle_area
        result = CalculateCompactness.shape_to_min_circle_at_shape(shape_area=circle_area, minimal_circle_area=minimal_circle_area)
        self.assertAlmostEqual(result, 1.0, delta=0.1)

    def test_digital_compactness_square(self):
        square_size = 4.0
        square_area = square_size ** 2
        circle_area = (np.pi * (square_size ** 2)) / 2
        result = CalculateCompactness.shape_to_min_circle_at_shape(shape_area=square_area, minimal_circle_area=circle_area)
        self.assertAlmostEqual(result, (2 / np.pi), delta=0.1)

    def test_digital_compactness(self):
        result = CalculateCompactness.shape_to_min_circle_at_shape(shape_area=78.0, minimal_circle_area=122.52)
        self.assertAlmostEqual(result, 0.63, delta=0.1)

    def test_perimeter_circle_to_perimeter_shape_fields_equal_for_circle(self):
        circle_area = np.pi
        circle_r = np.sqrt(circle_area / np.pi)
        circle_perimeter = 2 * np.pi * circle_r
        result = CalculateCompactness.perimeter_circle_to_perimeter_shape_fields_equal(shape_area=circle_area, shape_perimeter=circle_perimeter)
        self.assertAlmostEqual(result, 1.0, delta=0.1)

    def test_perimeter_circle_to_perimeter_shape_fields_equal_for_square(self):
        square_area = 16
        square_perimeter = 16
        result = CalculateCompactness.perimeter_circle_to_perimeter_shape_fields_equal(shape_area=square_area, shape_perimeter=square_perimeter)
        self.assertAlmostEqual(result, np.sqrt(np.pi) / 2, delta=0.1)


if __name__ == '__main__':
    unittest.main()
