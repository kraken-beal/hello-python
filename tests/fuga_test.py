# coding:utf-8

import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../lib')

from fuga import Fuga

class FugaTest(unittest.TestCase):

    def setUp(self):
         print('setUp')
         self.fuga = Fuga()

    def test_haiku(self):
        expected = "はむたまご はむはむたまご はむたまご"
        actual = self.fuga.haiku()
        self.assertEqual(actual, expected)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(FugaTest))
    return suite


if __name__ == '__main__':
    unittest.main()

