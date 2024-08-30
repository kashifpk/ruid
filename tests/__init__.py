import unittest
from ruid import ruid


class RuidTestCase(unittest.TestCase):
    def test_ruid_returns_string(self):
        result = ruid()
        self.assertIsInstance(result, str)

    def test_ruid_has_correct_length(self):
        result = ruid()
        self.assertEqual(len(result), 10)

    def test_length_below_6_raises_error(self):
        with self.assertRaises(ValueError):
            ruid(5)


if __name__ == '__main__':
    unittest.main()

