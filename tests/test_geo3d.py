import unittest
from math import sqrt, pi
import sys
import os

# Add the parent directory to the path to import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from demo_ci.geo3d import Cuboid, Pyramid, Sphere, Cylinder


class TestCuboid(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.cuboid1 = Cuboid(3, 4, 5)
        self.cuboid2 = Cuboid(2, 2, 2)  # Cube
        self.cuboid3 = Cuboid(1, 1, 1)  # Unit cube
    
    def test_cuboid_initialization(self):
        """Test that Cuboid objects are initialized correctly."""
        self.assertEqual(self.cuboid1.width, 3)
        self.assertEqual(self.cuboid1.height, 4)
        self.assertEqual(self.cuboid1.depth, 5)
    
    def test_cuboid_volume(self):
        """Test Cuboid volume calculation."""
        self.assertEqual(self.cuboid1.volume(), 60)  # 3 * 4 * 5 = 60
        self.assertEqual(self.cuboid2.volume(), 8)   # 2 * 2 * 2 = 8
        self.assertEqual(self.cuboid3.volume(), 1)   # 1 * 1 * 1 = 1
    
    def test_cuboid_surface_area(self):
        """Test Cuboid surface area calculation."""
        # Surface area = 2 * (wh + wd + hd)
        expected_sa1 = 2 * (3*4 + 3*5 + 4*5)  # 2 * (12 + 15 + 20) = 94
        self.assertEqual(self.cuboid1.surface_area(), expected_sa1)
        
        expected_sa2 = 2 * (2*2 + 2*2 + 2*2)  # 2 * (4 + 4 + 4) = 24
        self.assertEqual(self.cuboid2.surface_area(), expected_sa2)
        
        expected_sa3 = 2 * (1*1 + 1*1 + 1*1)  # 2 * (1 + 1 + 1) = 6
        self.assertEqual(self.cuboid3.surface_area(), expected_sa3)
    
    def test_cuboid_with_decimal_dimensions(self):
        """Test Cuboid with decimal dimensions."""
        cuboid_decimal = Cuboid(2.5, 3.2, 1.8)
        expected_volume = 2.5 * 3.2 * 1.8
        self.assertAlmostEqual(cuboid_decimal.volume(), expected_volume, places=2)


class TestPyramid(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.pyramid1 = Pyramid(6, 8, 10)
        self.pyramid2 = Pyramid(4, 4, 6)  # Square base
        self.pyramid3 = Pyramid(3, 3, 3)  # Small square pyramid
    
    def test_pyramid_initialization(self):
        """Test that Pyramid objects are initialized correctly."""
        self.assertEqual(self.pyramid1.base_width, 6)
        self.assertEqual(self.pyramid1.base_depth, 8)
        self.assertEqual(self.pyramid1.height, 10)
    
    def test_pyramid_volume(self):
        """Test Pyramid volume calculation."""
        # Volume = (1/3) * base_width * base_depth * height
        expected_vol1 = (1/3) * 6 * 8 * 10  # 160
        self.assertAlmostEqual(self.pyramid1.volume(), expected_vol1, places=2)
        
        expected_vol2 = (1/3) * 4 * 4 * 6  # 32
        self.assertAlmostEqual(self.pyramid2.volume(), expected_vol2, places=2)
        
        expected_vol3 = (1/3) * 3 * 3 * 3  # 9
        self.assertAlmostEqual(self.pyramid3.volume(), expected_vol3, places=2)
    
    def test_pyramid_surface_area(self):
        """Test Pyramid surface area calculation."""
        # This tests the current implementation
        area1 = self.pyramid1.surface_area()
        self.assertIsInstance(area1, float)
        self.assertGreater(area1, 0)
        
        area2 = self.pyramid2.surface_area()
        self.assertIsInstance(area2, float)
        self.assertGreater(area2, 0)


class TestSphere(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.sphere1 = Sphere(7)
        self.sphere2 = Sphere(1)  # Unit sphere
        self.sphere3 = Sphere(5)
    
    def test_sphere_initialization(self):
        """Test that Sphere objects are initialized correctly."""
        self.assertEqual(self.sphere1.radius, 7)
        self.assertEqual(self.sphere2.radius, 1)
    
    def test_sphere_volume(self):
        """Test Sphere volume calculation."""
        # Volume = (4/3) * π * r³
        # Note: The implementation uses 3.14159 instead of pi
        pi_approx = 3.14159
        
        expected_vol1 = (4/3) * pi_approx * (7 ** 3)
        self.assertAlmostEqual(self.sphere1.volume(), expected_vol1, places=1)
        
        expected_vol2 = (4/3) * pi_approx * (1 ** 3)
        self.assertAlmostEqual(self.sphere2.volume(), expected_vol2, places=2)
    
    def test_sphere_surface_area(self):
        """Test Sphere surface area calculation."""
        # Surface area = 4 * π * r²
        pi_approx = 3.14159
        
        expected_sa1 = 4 * pi_approx * (7 ** 2)
        self.assertAlmostEqual(self.sphere1.surface_area(), expected_sa1, places=1)
        
        expected_sa2 = 4 * pi_approx * (1 ** 2)
        self.assertAlmostEqual(self.sphere2.surface_area(), expected_sa2, places=2)
    
    def test_sphere_with_decimal_radius(self):
        """Test Sphere with decimal radius."""
        sphere_decimal = Sphere(2.5)
        volume = sphere_decimal.volume()
        surface_area = sphere_decimal.surface_area()
        
        self.assertIsInstance(volume, float)
        self.assertIsInstance(surface_area, float)
        self.assertGreater(volume, 0)
        self.assertGreater(surface_area, 0)


class TestCylinder(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.cylinder1 = Cylinder(5, 12)
        self.cylinder2 = Cylinder(3, 8)
        self.cylinder3 = Cylinder(1, 1)  # Unit cylinder
    
    def test_cylinder_initialization(self):
        """Test that Cylinder objects are initialized correctly."""
        self.assertEqual(self.cylinder1.radius, 5)
        self.assertEqual(self.cylinder1.height, 12)
    
    def test_cylinder_volume(self):
        """Test Cylinder volume calculation."""
        # Volume = π * r² * h
        pi_approx = 3.14159
        
        expected_vol1 = pi_approx * (5 ** 2) * 12
        self.assertAlmostEqual(self.cylinder1.volume(), expected_vol1, places=1)
        
        expected_vol2 = pi_approx * (3 ** 2) * 8
        self.assertAlmostEqual(self.cylinder2.volume(), expected_vol2, places=1)
        
        expected_vol3 = pi_approx * (1 ** 2) * 1
        self.assertAlmostEqual(self.cylinder3.volume(), expected_vol3, places=2)
    
    def test_cylinder_surface_area(self):
        """Test Cylinder surface area calculation."""
        # Surface area = 2 * π * r * (r + h)
        pi_approx = 3.14159
        
        expected_sa1 = 2 * pi_approx * 5 * (5 + 12)
        self.assertAlmostEqual(self.cylinder1.surface_area(), expected_sa1, places=1)
        
        expected_sa2 = 2 * pi_approx * 3 * (3 + 8)
        self.assertAlmostEqual(self.cylinder2.surface_area(), expected_sa2, places=1)
        
        expected_sa3 = 2 * pi_approx * 1 * (1 + 1)
        self.assertAlmostEqual(self.cylinder3.surface_area(), expected_sa3, places=2)
    
    def test_cylinder_with_decimal_dimensions(self):
        """Test Cylinder with decimal dimensions."""
        cylinder_decimal = Cylinder(2.5, 7.3)
        volume = cylinder_decimal.volume()
        surface_area = cylinder_decimal.surface_area()
        
        self.assertIsInstance(volume, float)
        self.assertIsInstance(surface_area, float)
        self.assertGreater(volume, 0)
        self.assertGreater(surface_area, 0)


if __name__ == '__main__':
    unittest.main()
