#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_max(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_list_str(self):
        self.assertRaises(TypeError, max_integer, [1, "hola"])

    def test_bool(self):
        self.assertEqual(max_integer([True, 4]), 4)

    def test_str(self):
        self.assertEqual(max_integer("hola"), 'o')

    def test_tuple(self):
        self.assertEqual(max_integer((1, 3, 4)), 4)

    def test_empty(self):
        self.assertEqual(max_integer(), None)

    def test_float(self):
        self.assertEqual(max_integer([1, 3.5, 4.65489743, 2]), 4.65489743)

    def test_multiple_args(self):
        self.assertRaises(TypeError, max_integer, [1, 3, 4], [1, 3, 5])
