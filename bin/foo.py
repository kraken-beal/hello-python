# coding:utf-8

import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../lib')

from fuga import Fuga



fuga = Fuga()
print(fuga.poem())