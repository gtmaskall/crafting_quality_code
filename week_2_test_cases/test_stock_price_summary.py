import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.

    # smallest test cases
    def test_stock_price_summary_0_length_input(self):
        """Test stock_price_summary with zero-length input"""

        actual = a1.stock_price_summary([])
        expected = (0.0, 0.0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_1_zero_int(self):
        """Test stock_price_summary with single integer zero change.

        Smallest case with zero change (as an integer)."""

        actual = a1.stock_price_summary([0])
        expected = (0.0, 0.0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_1_zero_float(self):
        """Test stock_price_summary with single float zero change.

        Smallest case with zero change (as a float)."""

        actual = a1.stock_price_summary([0.0])
        expected = (0.0, 0.0)
        self.assertEqual(actual, expected)


    def test_stock_price_summary_1_positive(self):
        """Test stock_price_summary with single positive change.

        Smallest positive change test case."""

        actual = a1.stock_price_summary([0.45])
        expected = (0.45, 0.0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_1_negative(self):
        """Test stock_price_summary with single negative change.

        Smallest negative change test case."""

        actual = a1.stock_price_summary([-0.42])
        expected = (0.0, -0.42)
        self.assertEqual(actual, expected)

    # smallest test cases with > 1 arg
    def test_stock_price_summary_2_zero(self):
        """Test stock_price_summary with two zero changes.

        Smallest multiple changes of zero test case.
        Combine int and float."""

        actual = a1.stock_price_summary([0, 0.0])
        expected = (0.0, 0.0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_2_positive(self):
        """Test stock_price_summary with two positive changes.

        Smallest multiple positive changes test case."""

        actual = a1.stock_price_summary([0.14, 0.21])
        expected = (0.35, 0.0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_2_negative(self):
        """Test stock_price_summary with two negative changes.

        Smallest multiple negative changes test case."""

        actual = a1.stock_price_summary([-0.15, -0.23])
        expected = (0.0, -0.38)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_1_negative_1_positive_A(self):
        """Test stock_price_summary with 1 negative and 1 positive change.

        First test order."""

        actual = a1.stock_price_summary([0.15, -0.23])
        expected = (0.15, -0.23)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_1_negative_1_positive_B(self):
        """Test stock_price_summary with 1 negative and 1 positive change.

        Reverse test order."""

        actual = a1.stock_price_summary([-0.23, 0.15])
        expected = (0.15, -0.23)
        self.assertEqual(actual, expected)

    # Finally, test cases where summation of both positive and negative required together
    def test_stock_price_summary_multiple_summation(self):
        """Test stock_price_summary with > 1 negative and > 1 positive change.

        Requires gathering together both cases and summing and ignoring zeros."""
        
        actual = a1.stock_price_summary([-0.23, 0.11, 0, -0.01, 0.0, -0.02, 0.0, 0.33])
        expected = (0.44, -0.26)


if __name__ == '__main__':
    unittest.main(exit=False)
