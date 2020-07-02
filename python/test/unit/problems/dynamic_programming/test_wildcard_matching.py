"""
Unit Test for wildcard_matching
"""
from unittest import TestCase

from problems.dynamic_programming.wildcard_matching import WildcardMatching


class TestWildcardMatching(TestCase):
    """
    Unit test for WildcardMatching
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestWildcardMatching

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "aa"
        pattern = "*"
        wildcard_matching_problem = WildcardMatching(input_string, pattern)

        # When
        result = wildcard_matching_problem.solve()

        # Then
        self.assertTrue(result)
