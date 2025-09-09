#!/usr/bin/env python3
"""
Test runner for the geo2d and geo3d modules.

This script runs all unit tests for the geometric calculation modules.
"""

import unittest
import sys
import os

# Add the parent directory to the path to import test modules
sys.path.insert(0, os.path.dirname(__file__))

from test_geo2d import TestRectangle, TestTriangle
from test_geo3d import TestCuboid, TestPyramid, TestSphere, TestCylinder


def run_all_tests():
    """Run all tests for geo2d and geo3d modules."""
    # Create a test suite
    test_suite = unittest.TestSuite()
    
    # Add geo2d tests
    test_suite.addTest(unittest.makeSuite(TestRectangle))
    test_suite.addTest(unittest.makeSuite(TestTriangle))
    
    # Add geo3d tests
    test_suite.addTest(unittest.makeSuite(TestCuboid))
    test_suite.addTest(unittest.makeSuite(TestPyramid))
    test_suite.addTest(unittest.makeSuite(TestSphere))
    test_suite.addTest(unittest.makeSuite(TestCylinder))
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Return whether all tests passed
    return result.wasSuccessful()


if __name__ == "__main__":
    print("Running all tests for geo2d and geo3d modules...")
    print("=" * 60)
    
    success = run_all_tests()
    
    if success:
        print("\n" + "=" * 60)
        print("All tests passed! ✓")
        sys.exit(0)
    else:
        print("\n" + "=" * 60)
        print("Some tests failed! ✗")
        sys.exit(1)
