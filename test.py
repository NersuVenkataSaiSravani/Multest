import unittest
from calculator import multiply_numbers

class TestMultiplication(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply_numbers(5, 4), 25)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply_numbers(5, 0), 0)


if __name__ == "__main__":
    unittest.main()
