import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file = read_file("inputs/test.txt")

    def testPart1(self):
        self.assertEqual(1156, lan_party_search(self.input_file))

    def testPart2(self):
        self.assertEqual("bx,cx,dr,dx,is,jg,km,kt,li,lt,nh,uf,um", lan_party_password(self.input_file))

    def testPart1Example1(self):
        self.assertEqual(7, lan_party_search(self.test_file))

    def testPart2Example1(self):
        self.assertEqual("co,de,ka,ta", lan_party_password(self.test_file))


if __name__ == "__main__":
    unittest.main()
