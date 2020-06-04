"""
Unit Test for swap_nodes_in_pairs
"""
from unittest import TestCase

from common.linked_list import LinkedList
from common.linked_list import Node
from problems.linked_list.swap_nodes_in_pairs import SwapNodesInPairs


class TestSwapNodesInPairs(TestCase):
    """
    Unit test for SwapNodesInPairs
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestSwapNodesInPairs

        Returns:
            None

        Raises:
            None
        """
        # Given
        elements_list = [1, 5, 7, 9, 15]
        input_list = LinkedList()
        for i in range(len(elements_list)):
            input_list.append(Node(elements_list[i]))

        swap_nodes_problem = SwapNodesInPairs(input_list)

        # When
        output_list = swap_nodes_problem.solve()

        # Then
        self.assertEqual(output_list, [5, 1, 9, 7, 15])
