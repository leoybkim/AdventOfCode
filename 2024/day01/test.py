import unittest
from solution import *

class Test(unittest.TestCase):
    def setUp(self):
        self.filename = "input.txt"

    def testPart1(self):
        self.assertEqual(2285373, find_total_distance(self.filename))

    def testPart2(self):
        self.assertEqual(21142653, find_similarity_score(self.filename))


if __name__ == "__main__":
    unittest.main()
