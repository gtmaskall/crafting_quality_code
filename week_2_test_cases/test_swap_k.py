import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_swap_k_emptyL(self):
        """Test swap_k with empty list input.

        Only possible value of k is 0"""

        L = []
        actual = a1.swap_k(L, 0)
        expected = []
        self.assertEqual(L, expected)

    def test_swap_k_L1_k0(self):
        """Test swap_k with single item list input.

        Only possible value of k is still 0"""

        L = [1]
        actual = a1.swap_k(L, 0)
        expected = [1]
        self.assertEqual(L, expected)

    def test_swap_k_L2_k0(self):
        """Test swap_k with shortest length L that's even
        
        First case with even length L, check it's unmodified"""

        L = [1, 2]
        actual = a1.swap_k(L, 0)
        expected = [1, 2]
        self.assertEqual(L, expected)

    def test_swap_k_L2_k1(self):
        """Test swap_k with shortest length L that's even with swapping.
        
        First time we can actually do a swap!"""

        L = [1, 2]
        actual = a1.swap_k(L, 1)
        expected = [2, 1]
        self.assertEqual(L, expected)

    def test_swap_k_L3_k0(self):
        """Test swap_k with shortest length L that's odd and > 1.
        
        Check we still get unmodified list"""

        L = [1, 2, 3]
        actual = a1.swap_k(L, 0)
        expected = [1, 2, 3]
        self.assertEqual(L, expected)

    def test_swap_k_L3_k1(self):
        """Test swap_k with shortest length L that's odd with swapping.
        
        First time we leave a middle value alone."""

        L = [1, 2, 3]
        actual = a1.swap_k(L, 1)
        expected = [3, 2, 1]
        self.assertEqual(L, expected)

    def test_swap_k_L4_k1(self):
        """Test swap_k with list length 4 and k = 1.
        
        First time we leave more than 1 middle value alone."""

        L = [1, 2, 3, 4]
        actual = a1.swap_k(L, 1)
        expected = [4, 2, 3, 1]
        self.assertEqual(L, expected)

    def test_swap_k_L4_k2(self):
        """Test swap_k with input length 4 and k = 2.
        
        First time we swap sublists with k > 1"""

        L = [1, 2, 3, 4]
        actual = a1.swap_k(L, 2)
        expected = [3, 4, 1, 2]
        self.assertEqual(L, expected)

    def test_swap_k_L5_k2(self):
        """Test swap_k with input length 5 and k = 2.
        
        First time with even swap length and odd length L."""

        L = [1, 2, 3, 4, 5]
        actual = a1.swap_k(L, 2)
        expected = [4, 5, 3, 1, 2]
        self.assertEqual(L, expected)

    def test_swap_k_L6_k2(self):
        """Test swap_k with list length 6 and k = 2.
        
        First time length of swap subregions and unchanged middle
        region all > 1 (even)"""

        L = [1, 2, 3, 4, 5, 6]
        actual = a1.swap_k(L, 2)
        expected = [5, 6, 3, 4, 1, 2]
        self.assertEqual(L, expected)

    def test_swap_k_L6_k3(self):
        """Test swap_k with list length 6 and k = 3.
        
        First time k is odd and > 1 (no unchanged middle items)"""

        L = [1, 2, 3, 4, 5, 6]
        actual = a1.swap_k(L, 3)
        expected = [4, 5, 6, 1, 2, 3]
        self.assertEqual(L, expected)

    def test_swap_k_L9_k3(self):
        """Test swap_k with list length 9 and k = 3.
        
        First time swap region lengths and unchanged middle
        region length all odd and > 1"""

        L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        actual = a1.swap_k(L, 3)
        expected = [7, 8, 9, 4, 5, 6, 1, 2, 3]
        self.assertEqual(L, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
