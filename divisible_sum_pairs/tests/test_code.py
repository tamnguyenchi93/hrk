import unittest
import sys
sys.path.append("..")

from my_code import divisibleSumPairs

class TestClass(unittest.TestCase):

    def test_case1(self):
        arr = [1, 3, 2, 6, 1, 2]
        k = 3
        result = divisibleSumPairs(len(arr), k, arr)
        expected = 5
        self.assertEqual(result, expected, "Should be %s" % (expected))

    def test_case2(self):
        arr = [1, 2, 3, 4, 5, 6]
        k = 5
        result = divisibleSumPairs(len(arr), k, arr)
        expected = 3
        self.assertEqual(result, expected, "Should be %s" % (expected))

    # def test_case3(self):
    #     s =[4]
    #     d = 4
    #     m = 1
    #     result = divisibleSumPairs(s, d, m)
    #     expected = 1
    #     self.assertEqual(result, expected, "Should be %s" % (expected))
if __name__ == '__main__':
    unittest.main()