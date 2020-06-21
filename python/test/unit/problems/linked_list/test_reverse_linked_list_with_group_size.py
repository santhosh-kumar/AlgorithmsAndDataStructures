"""
Unit Test for reverse_linked_list_with_group_size
"""
from unittest import TestCase

from common.linked_list import LinkedList
from common.linked_list import Node
from problems.linked_list.reverse_linked_list_with_group_size import ReverseLinkedListWithGroupSize


class TestReverseLinkedListWithGroupSize(TestCase):
    """
    Unit test for ReverseLinkedListWithGroupSize
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestReverseLinkedListWithGroupSize

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

        reverse_linked_list_problem = ReverseLinkedListWithGroupSize(input_list, 3)

        # When
        output_list = reverse_linked_list_problem.solve()

        # Then
        self.assertEqual(output_list, [7, 5, 1, 9, 15])
