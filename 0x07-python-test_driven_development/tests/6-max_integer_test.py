#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max = __import__('6-max_integer').max_integer
class Test_Max_Int(unittest.TestCase):
    """
    classs for testing the function max_integer by unittesting module
    """
    def test_normal_val(self):
        """
        normal values test
        """
        self.assertEqual(max([1, 3, 4, 7]), 7)
        self.assertEqual(max([1000, -3, -1]), 1000)
        self.assertEqual(max([-1, -3, -199]), -1)
        self.assertEqual(max([0]), 0)
    
    def test_moderate_val(self):
        """ list of lists, empty list, different type eleemets"""
        with self.assertRaises(TypeError):
            max(46)
        with self.assertRaises(TypeError):
            max([1, 2, "hi"])
        self.assertIsNone(max([]), None)
        self.assertEqual(max(["axy", "hbc"]), "hbc")

if __name__ == '__main__':
            unittest.main()
