#!/usr/bin/python3
"""
Test for rectangle.py
"""
import unittest
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):

    def setUp(self):
        Rectangle._Base__nb_objects = 0

    def test_make_rectangle(self):
        """
        check Rectangle no args
        """
        self.assertRaises(TypeError, Rectangle)

    def test_make_rectangle_12(self):
        """
        check Rectangle with 1 arg
        """
        self.assertRaises(TypeError, Rectangle, 5)

    def test_make_rectangle_args(self):
        """
        check Rectangle with 2 agrs
        """
        self.assertEqual(Rectangle(4, 5).id, 1)

    def test_rectangle_id_inc(self):
        """
        check if Rectangle id increment
        """
        b1 = Rectangle(4, 5)
        b2 = Rectangle(2, 4)
        self.assertEqual(b2.id, 4)

    def test_make_rectangle_args2(self):
        """
        check Rectangle with 3 agrs
        """
        self.assertEqual(Rectangle(4, 5, 1).id, 2)

    def test_rectangle_id_inc2(self):
        """
        check if Rectangle id increment
        """
        b1 = Rectangle(4, 5)
        b2 = Rectangle(2, 4, 0, 0, 12)
        b3 = Rectangle(2, 4)
        self.assertEqual(b2.id, 12)

    def test_rectangle_id_neg(self):
        """
        check Rectangle id negative
        """
        self.assertEqual(Rectangle(2, 4, 0, 0, -1).id, -1)

    def test_str(self):
        """
        check Rectangle with str
        """
        self.assertRaises(TypeError, Rectangle, "hola")

    def test_neg(self):
        """
        check Rectangle with negative
        """
        self.assertRaises(ValueError, Rectangle, -1, -1)
    
    def test_neg_pos(self):
        """
        check Rectangle with negative position
        """
        self.assertRaises(ValueError, Rectangle, 10, 10, -1, -1)

if __name__ == '__main__':
    unittest.main()