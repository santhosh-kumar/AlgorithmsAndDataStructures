"""
Unit Test for two_sum
"""
from unittest import TestCase

from problems.sampling.reservoir import ReservoirSampling


class TestReservoirSampling(TestCase):
    """
    Unit test for ReservoirSampling
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestReservoirSampling

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [i for i in range(100)]
        number_samples = 10
        sampling_problem = ReservoirSampling(input_list, number_samples)

        # When
        result = sampling_problem.solve()

        # Then
        self.assertEqual(len(set(result)), number_samples)
