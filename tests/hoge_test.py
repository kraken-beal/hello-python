# coding:utf-8

import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../lib')

from fuga import Fuga

class HogeTest(unittest.TestCase):

    def setUp(self):
         print('setUp')
         self.fuga = Fuga()

    def test_first(self):
        print('test_first')

    def test_fuga(self):
        actual = self.fuga.index()
        self.assertTrue(actual)
    
    def test_poem(self):
        expected = "spam spam spam"
        actual = self.fuga.poem()
        self.assertEqual(actual, expected)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(HogeTest))
    return suite


if __name__ == '__main__':
    unittest.main()

