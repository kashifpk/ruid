import unittest
from ruid import ruid


class RuidTestCase(unittest.TestCase):
    def test_ruid_returns_string(self):
        result = ruid()
        self.assertIsInstance(result, str)

    def test_ruid_has_correct_length(self):
        result = ruid()
        self.assertEqual(len(result), 10)

    def test_length_below_6(self):
        result = ruid(5)
        result2 = ruid(5)

        self.assertIsInstance(result, str)
        self.assertIsInstance(result2, str)
        self.assertEqual(len(result), 5)
        self.assertEqual(len(result2), 5)
        self.assertNotEqual(result[:4], result2[:4])


if __name__ == '__main__':
    unittest.main()

