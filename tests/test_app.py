from app import greet
import unittest
import sys
import os

# Dynamically add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(
            greet("World"), "Hello, World from FirstName LastName!")


if __name__ == "__main__":
    unittest.main()
