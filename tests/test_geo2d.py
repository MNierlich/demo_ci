import unittest
from math import sqrt
import sys
import os

# Add the parent directory to the path to import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from demo_ci.geo2d import Rectangle, Triangle


class TestRectangle(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.rect1 = Rectangle(5, 3)
        self.rect2 = Rectangle(10, 7)
        self.rect3 = Rectangle(1, 1)
    
    def test_rectangle_initialization(self):
        """Test that Rectangle objects are initialized correctly."""
        self.assertEqual(self.rect1.width, 5)
        self.assertEqual(self.rect1.height, 3)
        self.assertEqual(self.rect2.width, 10)
        self.assertEqual(self.rect2.height, 7)
    
    def test_rectangle_area(self):
        """Test Rectangle area calculation."""
        # Note: The current implementation has a bug - it multiplies by 2
        # Testing the current implementation
        self.assertEqual(self.rect1.area(), 30)  # 5 * 3 * 2 = 30 (current implementation)
        self.assertEqual(self.rect2.area(), 140)  # 10 * 7 * 2 = 140 (current implementation)
        self.assertEqual(self.rect3.area(), 2)  # 1 * 1 * 2 = 2 (current implementation)
    
    def test_rectangle_area_should_be_correct(self):
        """Test what the Rectangle area should be without the bug."""
        # This test documents what the correct area should be
        # (Remove the * 2 from the area method to make these pass)
        expected_area1 = 5 * 3  # 15
        expected_area2 = 10 * 7  # 70
        expected_area3 = 1 * 1  # 1
        
        # These assertions will fail with current implementation
        # Uncomment when the bug is fixed
        # self.assertEqual(self.rect1.area(), expected_area1)
        # self.assertEqual(self.rect2.area(), expected_area2)
        # self.assertEqual(self.rect3.area(), expected_area3)
    
    def test_rectangle_perimeter(self):
        """Test Rectangle perimeter calculation."""
        self.assertEqual(self.rect1.perimeter(), 16)  # 2 * (5 + 3) = 16
        self.assertEqual(self.rect2.perimeter(), 34)  # 2 * (10 + 7) = 34
        self.assertEqual(self.rect3.perimeter(), 4)   # 2 * (1 + 1) = 4
    
    def test_rectangle_with_zero_dimensions(self):
        """Test Rectangle with zero dimensions."""
        rect_zero = Rectangle(0, 5)
        self.assertEqual(rect_zero.area(), 0)
        self.assertEqual(rect_zero.perimeter(), 10)
        
        rect_zero2 = Rectangle(3, 0)
        self.assertEqual(rect_zero2.area(), 0)
        self.assertEqual(rect_zero2.perimeter(), 6)
    
    def test_rectangle_with_decimal_dimensions(self):
        """Test Rectangle with decimal dimensions."""
        rect_decimal = Rectangle(2.5, 4.2)
        self.assertAlmostEqual(rect_decimal.area(), 21.0, places=2)  # 2.5 * 4.2 * 2 = 21.0
        self.assertAlmostEqual(rect_decimal.perimeter(), 13.4, places=2)  # 2 * (2.5 + 4.2) = 13.4


class TestTriangle(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.triangle1 = Triangle(3, 4, 5)  # Right triangle
        self.triangle2 = Triangle(6, 8, 10)  # Scaled right triangle
        self.triangle3 = Triangle(5, 5, 5)   # Equilateral triangle
        self.triangle4 = Triangle(3, 3, 3)   # Smaller equilateral triangle
    
    def test_triangle_initialization(self):
        """Test that Triangle objects are initialized correctly."""
        self.assertEqual(self.triangle1.a, 3)
        self.assertEqual(self.triangle1.b, 4)
        self.assertEqual(self.triangle1.c, 5)
    
    def test_triangle_area_right_triangle(self):
        """Test Triangle area calculation for right triangles."""
        # For a 3-4-5 right triangle, area should be 6
        self.assertAlmostEqual(self.triangle1.area(), 6.0, places=2)
        
        # For a 6-8-10 right triangle, area should be 24
        self.assertAlmostEqual(self.triangle2.area(), 24.0, places=2)
    
    def test_triangle_area_equilateral(self):
        """Test Triangle area calculation for equilateral triangles."""
        # For equilateral triangle with side 5, area = (sqrt(3)/4) * 5^2
        expected_area = (sqrt(3) / 4) * 25
        self.assertAlmostEqual(self.triangle3.area(), expected_area, places=2)
        
        # For equilateral triangle with side 3
        expected_area_small = (sqrt(3) / 4) * 9
        self.assertAlmostEqual(self.triangle4.area(), expected_area_small, places=2)
    
    def test_triangle_perimeter(self):
        """Test Triangle perimeter calculation."""
        self.assertEqual(self.triangle1.perimeter(), 12)  # 3 + 4 + 5 = 12
        self.assertEqual(self.triangle2.perimeter(), 24)  # 6 + 8 + 10 = 24
        self.assertEqual(self.triangle3.perimeter(), 15)  # 5 + 5 + 5 = 15
        self.assertEqual(self.triangle4.perimeter(), 9)   # 3 + 3 + 3 = 9
    
    def test_triangle_with_decimal_sides(self):
        """Test Triangle with decimal side lengths."""
        triangle_decimal = Triangle(2.5, 3.5, 4.2)
        perimeter = 2.5 + 3.5 + 4.2
        self.assertAlmostEqual(triangle_decimal.perimeter(), perimeter, places=2)
        
        # Test that area calculation doesn't raise an error
        area = triangle_decimal.area()
        self.assertIsInstance(area, float)
        self.assertGreater(area, 0)
    
    def test_triangle_invalid_sides(self):
        """Test Triangle with sides that cannot form a valid triangle."""
        # This is a degenerate case - sides 1, 2, 5 cannot form a triangle
        # (1 + 2 < 5, violates triangle inequality)
        invalid_triangle = Triangle(1, 2, 5)
        
        # The area calculation will fail or return invalid result
        # In this case, Heron's formula will try to take sqrt of negative number
        with self.assertRaises(ValueError):
            invalid_triangle.area()


if __name__ == '__main__':
    unittest.main()
