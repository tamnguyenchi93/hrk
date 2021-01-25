import unittest
import sys
sys.path.append("..")

from my_code import getTotalX

class TestGetTotalX(unittest.TestCase):

    def test_case1(self):
        a = [2, 4]
        b = [16, 32, 96]
        c = getTotalX(a, b)
        self.assertEqual(c, 3, "Should be %d" % (3))

    def test_case2(self):
        a = [3, 4]
        b = [24, 48]
        c = getTotalX(a, b)
        self.assertEqual(c, 2, "Should be %d" % (2))

if __name__ == '__main__':
    unittest.main()