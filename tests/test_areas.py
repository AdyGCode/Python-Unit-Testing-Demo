# -------------------------------------------------------------------
# Project:    Python-Unit-Testing-Demo
# Filename:   test_areas.py
# Location:   ./tests
# Author:     Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
# Created:    2024-05-10
# Purpose:
#    This file provides the following features, methods and associated 
#    supporting code:
#    
# ---------------------------------------------------------------------
import unittest
from areas import Areas
from math import pi

class TestAreas(unittest.TestCase):

    def setUp(self):


    def test_area_circle(self):
        # Radius >= 0
        area = Areas()
        self.assertAlmostEqual(area.area_circle(1), pi)
        self.assertAlmostEqual(area.area_circle(0), 0)
        self.assertAlmostEqual(area.area_circle(2.1), pi * 2.1 * 2.1)


if __name__ == '__main__':
    unittest.main()
