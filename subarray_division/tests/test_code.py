import unittest
import sys
sys.path.append("..")

from my_code import birthday

class TestBirthday(unittest.TestCase):

    def test_case1(self):
        s =[1, 2, 1, 3, 2]
        d = 3
        m = 2
        result = birthday(s, d, m)
        expected = 2
        self.assertEqual(result, expected, "Should be %s" % (expected))

    def test_case2(self):
        s =[1, 1, 1, 1, 1, 1]
        d = 3
        m = 2
        result = birthday(s, d, m)
        expected = 0
        self.assertEqual(result, expected, "Should be %s" % (expected))

    def test_case3(self):
        s =[4]
        d = 4
        m = 1
        result = birthday(s, d, m)
        expected = 1
        self.assertEqual(result, expected, "Should be %s" % (expected))
if __name__ == '__main__':
    unittest.main()