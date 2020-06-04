"""
Unit Test for merge_two_sorted_linked_lists
"""
from unittest import TestCase

from common.linked_list import LinkedList
from common.linked_list import Node
from problems.linked_list.merge_two_sorted_linked_lists import MergeTwoSortedLinkedLists


class TestMergeTwoSortedLinkedLists(TestCase):
    """
    Unit test for MergeTwoSortedLinkedLists
    """

    def test_solve(self):
        """Test solve

        Args:
            self: MergeTwoSortedLinkedLists

        Returns:
            None

        Raises:
            None
        """
        # Given
        elements_list1 = [1, 5, 7, 9, 15, 17]
        input_list1 = LinkedList()
        for i in range(len(elements_list1)):
            input_list1.append(Node(elements_list1[i]))

        elements_list2 = [2, 3, 3, 6]
        input_list2 = LinkedList()
        for i in range(len(elements_list2)):
            input_list2.append(Node(elements_list2[i]))

        merge_linked_list_problem = MergeTwoSortedLinkedLists(input_list1, input_list2)

        # When
        output_list = merge_linked_list_problem.solve()

        # Then
        self.assertEqual(output_list, [1, 2, 3, 3, 5, 6, 7, 9, 15, 17])
