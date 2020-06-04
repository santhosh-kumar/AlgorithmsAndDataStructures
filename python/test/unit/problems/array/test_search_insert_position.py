"""
Unit Test for search_insert_position
"""
from unittest import TestCase

from problems.array.search_insert_position import SearchInsertPosition


class TestSearchInsertPosition(TestCase):
    """
    Unit test for SearchInsertPosition
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestSearchInsertPosition

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [1, 3, 5, 6]
        search_insert_problem = SearchInsertPosition(input_list, 5)

        # When
        position = search_insert_problem.solve()

        # Then
        self.assertEqual(position, 2)

    def test_solve_new_element(self):
        """Test solve (new element)

        Args:
            self: TestSearchInsertPosition

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [1, 3, 5, 6]
        search_insert_problem = SearchInsertPosition(input_list, 2)

        # When
        position = search_insert_problem.solve()

        # Then
        self.assertEqual(position, 1)

    def test_solve_end_element(self):
        """Test solve (end element)

        Args:
            self: TestSearchInsertPosition

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [1, 3, 5, 6]
        search_insert_problem = SearchInsertPosition(input_list, 7)

        # When
        position = search_insert_problem.solve()

        # Then
        self.assertEqual(position, 4)

    def test_solve_first_element(self):
        """Test solve (first element)

        Args:
            self: TestSearchInsertPosition

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [1, 3, 5, 6]
        search_insert_problem = SearchInsertPosition(input_list, 0)

        # When
        position = search_insert_problem.solve()

        # Then
        self.assertEqual(position, 0)
