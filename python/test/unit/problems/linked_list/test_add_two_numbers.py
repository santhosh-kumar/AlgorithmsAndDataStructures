"""
Unit Test for add_two_numbers
"""
from unittest import TestCase

from common.linked_list import LinkedList
from common.linked_list import Node
from problems.linked_list.add_two_numbers import AddTwoNumbers


class TestAddTwoNumbers(TestCase):
    """
    Unit test for AddTwoNumbers
    """

    def test_solve(self):
        """Test solve

        Args:
            self: AddTwoNumbers

        Returns:
            None

        Raises:
            None
        """
        # Given
        elements_list1 = [2, 4, 3]
        input_list1 = LinkedList()
        for i in range(len(elements_list1)):
            input_list1.append(Node(elements_list1[i]))

        elements_list2 = [5, 6, 4]
        input_list2 = LinkedList()
        for i in range(len(elements_list2)):
            input_list2.append(Node(elements_list2[i]))

        add_two_numbers_problem = AddTwoNumbers(input_list1, input_list2)

        # When
        total = add_two_numbers_problem.solve()

        # Then
        self.assertEqual(total, [8, 0, 7])

    def test_solve_overflow(self):
        """Test solve (overflow)

        Args:
            self: AddTwoNumbers

        Returns:
            None

        Raises:
            None
        """
        # Given
        elements_list1 = [2, 4, 3]
        input_list1 = LinkedList()
        for i in range(len(elements_list1)):
            input_list1.append(Node(elements_list1[i]))

        elements_list2 = [5, 6, 4, 3]
        input_list2 = LinkedList()
        for i in range(len(elements_list2)):
            input_list2.append(Node(elements_list2[i]))

        add_two_numbers_problem = AddTwoNumbers(input_list1, input_list2)

        # When
        total = add_two_numbers_problem.solve()

        # Then
        self.assertEqual(total, [3, 8, 0, 7])
