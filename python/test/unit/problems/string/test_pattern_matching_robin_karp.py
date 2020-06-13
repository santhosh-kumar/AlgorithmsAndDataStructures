"""
Unit Test for strstr
"""
from unittest import TestCase

from problems.string.pattern_matching_rabin_karp import PatternMatchingRabinKarpAlgorithm


class TestPatternMatchingRabinKarpAlgorithm(TestCase):
    """
    Unit test for PatternMatchingRabinKarpAlgorithm
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestPatternMatchingRabinKarpAlgorithm

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "mississippi"
        needle = "issi"
        pattern_matching_problem = PatternMatchingRabinKarpAlgorithm(input_string, needle)

        # When
        index = pattern_matching_problem.solve()

        # Then
        self.assertEqual(index, 2)
