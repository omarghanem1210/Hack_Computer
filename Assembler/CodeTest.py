import unittest
from Code import *


class MyTestCase(unittest.TestCase):
    def testDest(self):
        self.assertEqual('111', dest('ADM'))
        self.assertEqual('000', dest('null'))
        self.assertEqual('011', dest('DM'))
        self.assertEqual('100', dest('A'))

    def testComp(self):
        self.assertEqual('0001110', comp('D-1'))
        self.assertEqual('1010101', comp('D|M'))

    def testJump(self):
        self.assertEqual('111', jump('JMP'))
        self.assertEqual('110', jump('JLE'))
