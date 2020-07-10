"""
Unit Test for all_unique_permutations
"""
from unittest import TestCase

from problems.backtracking.all_unique_permutations import AllUniquePermutations


class TestAllUniquePermutations(TestCase):
    """
    Unit test for AllUniquePermutations
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestAllUniquePermutations

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [1, 2, 3]
        permutation_problem = AllUniquePermutations(input_list)

        # When
        result = permutation_problem.solve()

        # Then
        self.assertEqual(result, [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
