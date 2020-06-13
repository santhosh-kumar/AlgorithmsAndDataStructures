"""
Unit Test for strstr
"""
from unittest import TestCase

from problems.string.pattern_matching_kmp import PatternMatchingKMPAlgorithm


class TestPatternMatchingKMPAlgorithm(TestCase):
    """
    Unit test for PatternMatchingKMPAlgorithm
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestPatternMatchingKMPAlgorithm

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "mississippi"
        needle = "issi"
        pattern_matching_problem = PatternMatchingKMPAlgorithm(input_string, needle)

        # When
        index = pattern_matching_problem.solve()

        # Then
        self.assertEqual(index, [1, 4])
