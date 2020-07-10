"""
Unit Test for combination_sum
"""
from unittest import TestCase

from problems.backtracking.generate_all_parantheses import GenerateAllParantheses


class TestGenerateAllParantheses(TestCase):
    """
    Unit test for GenerateAllParantheses
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestGenerateAllParantheses

        Returns:
            None

        Raises:
            None
        """
        # Given
        n = 3
        generate_all_problem = GenerateAllParantheses(n)

        # When
        result = generate_all_problem.solve()

        # Then
        self.assertEqual(result, ['((()))', '(()())', '(())()', '()(())', '()()()'])
