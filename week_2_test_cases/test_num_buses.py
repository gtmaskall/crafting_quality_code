import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.

    def test_num_buses_0(self):
        """Test num_buses with 0 passengers"""

        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_num_buses_1(self):
        """Test num_buses with 1 passenger"""

        actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_num_buses_2(self):
        """Test num_buses with 2 passengers
        
        Smallest test case with more than 1 passenger."""

        actual = a1.num_buses(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_num_buses_15(self):
        """Test num_buses with 15 passengers
        
        Mid-range number of passengers for a bus."""

        actual = a1.num_buses(15)
        expected = 1
        self.assertEqual(actual, expected)

    def test_num_buses_50(self):
        """Test num_buses with 50 passengers.
        
        Maximum number of passengers for just one bus.
        """

        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)

    def test_num_buses_51(self):
        """Test num_buses with 51 passengers.
        
        Boundary case. Smallest number of passengers now requiring
        two buses.
        """

        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(actual, expected)

    def test_num_buses_75(self):
        """Test num_buses with 75 passengers.
        
        Mid-range number of passengers for two buses."""

        actual = a1.num_buses(75)
        expected = 2
        self.assertEqual(actual, expected)

    def test_num_buses_201(self):
        """Test num_buses with 201 passengers.
        
        Largeish number of passengers (just) requiring 5 buses."""

        actual = a1.num_buses(201)
        expected = 5
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
