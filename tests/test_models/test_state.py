#!/usr/bin/python3
""" """
import unittest
from models.state import State


class test_state(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
