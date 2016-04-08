import unittest
from jelly import jelly_eval

class BasicParsingTests(unittest.TestCase):
    def test_nilad(self):
        self.assertEqual(3, jelly_eval("3", []))

    def test_explict_monad(self):
        self.assertEqual(3, jelly_eval("6H", []))

    def test_explicit_dyad(self):
        self.assertEqual(3, jelly_eval("1+2", []))

    def test_implicit_monad(self):
        self.assertEqual(2, jelly_eval("H", [4]))

    def test_implicit_dyad(self):
        self.assertEqual(5, jelly_eval("+", [2, 3]))

class ParseMonadtests(unittest.TestCase):
    def test_chained(self):
        self.assertEqual(2, jelly_eval("HH", [8]))
        self.assertEqual(1, jelly_eval("HHH", [8]))


if __name__ == '__main__':
    unittest.main()
