#!/usr/bin/python3
"""
Test for base.py
"""
import unittest
from models.base import Base


class test_base(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_make_base(self):
        """
        check if base id no args
        """
        self.assertEqual(Base().id, 1)

    def test_make_base_12(self):
        """
        check if base id with 1 arg
        """
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_make_base_args(self):
        """
        check if base id with 2 agrs
        """
        self.assertRaises(TypeError, Base, 12, 4)

    def test1_base_id_inc(self):
        """
        check if base id increment
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test2_base_id_inc2(self):
        """
        check if base id increment
        """
        b1 = Base()
        b2 = Base(10)
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_base_id_neg(self):
        """
        check base id negaative
        """
        self.assertEqual(Base(-1).id, -1)

if __name__ == '__main__':
    unittest.main()