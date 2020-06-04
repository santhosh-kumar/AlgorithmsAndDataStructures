"""
Unit Test for merge_k_sorted_linked_lists_priority_queue
"""
from unittest import TestCase

from common.linked_list import LinkedList
from common.linked_list import Node
from problems.linked_list.merge_k_sorted_linked_lists_priority_queue import MergeKSortedLinkedListsPriorityQueue


class TestMergeKSortedLinkedListsPriorityQueue(TestCase):
    """
    Unit test for MergeKSortedLinkedListsPriorityQueue
    """

    def test_solve(self):
        """Test solve

        Args:
            self: MergeKSortedLinkedListsPriorityQueue

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

        elements_list3 = [4, 6, 8, 10, 12, 14, 16, 18]
        input_list3 = LinkedList()
        for i in range(len(elements_list3)):
            input_list3.append(Node(elements_list3[i]))

        input_linked_lists_list = [input_list1, input_list2, input_list3]

        merge_k_linked_lists_problem = MergeKSortedLinkedListsPriorityQueue(input_linked_lists_list)

        # When
        output_list = merge_k_linked_lists_problem.solve()

        # Then
        self.assertEqual(output_list, [1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18])
