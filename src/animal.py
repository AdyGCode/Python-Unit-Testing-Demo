# -------------------------------------------------------------------
# Project:    Python-Unit-Testing-Demo
# Filename:   animal.py
# Location:   ./src
# Author:     Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
# Created:    2024-05-10
# Purpose:
#    This file provides the following features, methods and associated 
#    supporting code:
#    
# ---------------------------------------------------------------------

class Animal:
    _name = "OOPS"
    def __init__(self, name=""):
        self._name = name

    def name(self):
        return _name
