import unittest
import math
from kaleidoscope import rotate_point # Assuming kaleidoscope.py is in the same directory or PYTHONPATH

class TestKaleidoscope(unittest.TestCase):

    def test_rotate_point_no_rotation(self):
        # Test rotation by 0 degrees
        center = (0, 0)
        point = (10, 0)
        angle_rad = 0
        self.assertEqual(rotate_point(point, center, angle_rad), point)

        center_offset = (50, 50)
        point_offset = (60, 50) # 10 units to the right of center_offset
        self.assertEqual(rotate_point(point_offset, center_offset, angle_rad), point_offset)

    def test_rotate_point_360_rotation(self):
        # Test rotation by 360 degrees (2 * pi radians)
        center = (0, 0)
        point = (10, 20)
        angle_rad = 2 * math.pi
        # Due to potential floating point inaccuracies, check if points are close
        rotated = rotate_point(point, center, angle_rad)
        self.assertAlmostEqual(rotated[0], point[0], places=5)
        self.assertAlmostEqual(rotated[1], point[1], places=5)

        center_offset = (30, -30)
        point_offset = (100, 100)
        rotated_offset = rotate_point(point_offset, center_offset, angle_rad)
        self.assertAlmostEqual(rotated_offset[0], point_offset[0], places=5)
        self.assertAlmostEqual(rotated_offset[1], point_offset[1], places=5)


    def test_rotate_point_90_degrees_around_origin(self):
        center = (0, 0)
        point = (10, 0) # On X-axis
        angle_rad = math.pi / 2 # 90 degrees
        expected_point = (0, 10) # Should rotate to Y-axis
        rotated = rotate_point(point, center, angle_rad)
        self.assertAlmostEqual(rotated[0], expected_point[0], places=5)
        self.assertAlmostEqual(rotated[1], expected_point[1], places=5)

        point = (0, 20) # On Y-axis
        expected_point_2 = (-20, 0) # Should rotate to -X-axis
        rotated_2 = rotate_point(point, center, angle_rad)
        self.assertAlmostEqual(rotated_2[0], expected_point_2[0], places=5)
        self.assertAlmostEqual(rotated_2[1], expected_point_2[1], places=5)

    def test_rotate_point_180_degrees_around_origin(self):
        center = (0, 0)
        point = (10, 5)
        angle_rad = math.pi # 180 degrees
        expected_point = (-10, -5)
        rotated = rotate_point(point, center, angle_rad)
        self.assertAlmostEqual(rotated[0], expected_point[0], places=5)
        self.assertAlmostEqual(rotated[1], expected_point[1], places=5)

    def test_rotate_point_90_degrees_offset_center(self):
        center = (5, 5)
        point = (15, 5)  # 10 units to the right of center, on its horizontal line
        angle_rad = math.pi / 2 # 90 degrees
        # Expected: point relative to center is (10,0). Rotated: (0,10).
        # Add back center: (0+5, 10+5) = (5, 15)
        expected_point = (5, 15)
        rotated = rotate_point(point, center, angle_rad)
        self.assertAlmostEqual(rotated[0], expected_point[0], places=5)
        self.assertAlmostEqual(rotated[1], expected_point[1], places=5)

    # A simple test for the click storage mechanism might be harder without Pygame running.
    # We can add a placeholder or skip it if it's too complex for now.
    # For now, the focus is on `rotate_point`.

if __name__ == '__main__':
    unittest.main()
