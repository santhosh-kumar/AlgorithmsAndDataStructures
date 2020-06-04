"""
Unit Test for two_sum
"""
from unittest import TestCase

from problems.string.atoi import AtoI


class TestAtoI(TestCase):
    """
    Unit test for AtoI
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestAtoI

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "    +23972749"
        atoi_problem = AtoI(input_string)

        # When
        number = atoi_problem.solve()

        # Then
        self.assertEqual(number, 23972749)

    def test_solve_max_int(self):
        """Test solve (max int)

        Args:
            self: TestAtoI

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "    +239727493535353535343434"
        atoi_problem = AtoI(input_string)

        # When
        number = atoi_problem.solve()

        # Then
        self.assertEqual(number, AtoI.MAX_INT_VALUE)

    def test_solve_min_int(self):
        """Test solve (min int)

        Args:
            self: TestAtoI

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "    -239727493535353535343434"
        atoi_problem = AtoI(input_string)

        # When
        number = atoi_problem.solve()

        # Then
        self.assertEqual(number, AtoI.MIN_INT_VALUE)
