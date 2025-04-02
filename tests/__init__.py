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

    def test_fully_random_parameter(self):
        # Generate multiple IDs in the same second
        results = [ruid(10, fully_random=True) for _ in range(10)]

        # Check all have correct length
        for result in results:
            self.assertIsInstance(result, str)
            self.assertEqual(len(result), 10)

        # Check that the last 6 characters differ between IDs
        # This confirms they don't all have the same time encoding
        for i in range(len(results) - 1):
            self.assertNotEqual(results[i][-6:], results[i+1][-6:])

    def test_compare_regular_and_fully_random(self):
        # Standard time-encoded ID
        regular_ids = [ruid(10) for _ in range(5)]

        # Check that time-encoded IDs have same last 6 characters
        for i in range(len(regular_ids) - 1):
            self.assertEqual(regular_ids[i][-6:], regular_ids[i+1][-6:])

        # Fully random IDs should be different
        random_ids = [ruid(10, fully_random=True) for _ in range(5)]
        for i in range(len(random_ids) - 1):
            # There's a small chance this could fail randomly
            # but it's very unlikely
            self.assertNotEqual(random_ids[i][-6:], random_ids[i+1][-6:])


if __name__ == '__main__':
    unittest.main()

