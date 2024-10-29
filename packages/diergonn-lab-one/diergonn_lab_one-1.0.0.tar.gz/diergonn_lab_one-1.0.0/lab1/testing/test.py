"""Module providing a function to test main.py."""

import unittest
from lab1.main import even

class TestStringMethods(unittest.TestCase):
    """Function to test main.py."""

    def test_odd_even(self):
        """Function to test array a of mix of odd and even numbers."""
        self.assertEqual(even({"data": [1,2,3,4,5,6,7,8,9,10]}), [2,4,6,8,10])

    def test_even_only(self):
        """Function to test array of even numbers."""
        self.assertEqual(even({"data": [2,4,6,8,10]}), [2,4,6,8,10])

    def test_odd_only(self):
        """Function to test array of odd numbers."""
        self.assertEqual(even({"data": [1,3,5,7,9]}), [])

    def test_empty_array(self):
        """Function to test array of odd numbers."""
        self.assertEqual(even({"data": []}), [])

if __name__ == '__main__':
    unittest.main()
