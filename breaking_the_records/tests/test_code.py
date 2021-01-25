import unittest
import sys
sys.path.append("..")

from my_code import breakingRecords

class TestGetTotalX(unittest.TestCase):

    def test_case1(self):
        a = [10, 5, 20, 20, 4, 5, 2, 25, 1]
        c = breakingRecords(a)
        self.assertListEqual(c, [2, 4], "Should be %s" % ([2, 4]))

    def test_case2(self):
        a = [3 ,4, 21, 36, 10, 28, 35, 5, 24, 42]
        c = breakingRecords(a)
        self.assertListEqual(c, [4, 0], "Should be %s" % ([4, 0]))

if __name__ == '__main__':
    unittest.main()