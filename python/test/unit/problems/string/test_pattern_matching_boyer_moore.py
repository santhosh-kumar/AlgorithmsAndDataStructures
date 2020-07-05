"""
Unit Test for pattern_matching_boyer_moore
"""
from unittest import TestCase

from problems.string.pattern_matching_boyer_moore import PatternMatchingBoyerMooreAlgorithm


class TestPatternMatchingBoyerMooreAlgorithm(TestCase):
    """
    Unit test for PatternMatchingBoyerMooreAlgorithm
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestPatternMatchingBoyerMooreAlgorithm

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "mississippi"
        needle = "issi"
        pattern_matching_problem = PatternMatchingBoyerMooreAlgorithm(input_string, needle)

        # When
        index = pattern_matching_problem.solve()

        # Then
        self.assertEqual(index, 2)
