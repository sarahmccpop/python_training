from divisible import divisible_by
import unittest

# have to pass unittest.TestCase to the class
class TestDivisible(unittest.TestCase):
    def test_divisible_by(self):
        self.assertTrue(divisible_by(10, 2))
        self.assertFalse(divisible_by(10, 3))


if __name__ == "__main__":
    unittest.main()
