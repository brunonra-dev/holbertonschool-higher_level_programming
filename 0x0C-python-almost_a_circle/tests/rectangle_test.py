#!/usr/bin/python3
"""
Test for rectangle.py
"""
import unittest
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):

    def make_rectangle(self):
        """
        check if base id no args
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(print(b1.id), 1)

    def make_rectangle_id(self):
        """
        check if base id with id
        """
        b1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(print(b1.id), 12)

    def make_base_arg(self):
        """
        check base id with 1 agrs
        """
        self.assertRaises(TypeError, Base, 12)

    def base_id_inc(self):
        """
        check if base id increment
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(print(b2.id), 2)

    def base_id_inc2(self):
        """
        check if base id increment
        """
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(print(b2.id), 2)

    def base_id_neg(self):
        """
        check base id negaative
        """
        b1 = Base(-1)
        self.assertEqual(print(b1.id), -1)

    def base_id_str(self):
        """
        check base id str
        """
        self.assertRaises(TypeError, Base, "hola")

    def base_id_float(self):
        """
        check base id float
        """
        self.assertRaises(TypeError, Base, 1.0)

    def base_id_bool(self):
        """
        check base id bool
        """
        self.assertRaises(TypeError, Base, True)
