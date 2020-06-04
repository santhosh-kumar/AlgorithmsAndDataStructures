"""
Unit Test for copy_list_with_random_pointer
"""
from unittest import TestCase

from common.linked_list import LinkedList
from common.linked_list import Node
from problems.linked_list.copy_list_with_random_pointer import CopyListWithRandomPointer


class TestCopyListWithRandomPointer(TestCase):
    """
    Unit test for CopyListWithRandomPointer
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestCopyListWithRandomPointer

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_linked_list = LinkedList()
        input_linked_list.append(Node(1))
        input_linked_list.append(Node(2))
        input_linked_list.append(Node(3))
        input_linked_list.append(Node(4))
        input_linked_list.append(Node(5))

        # 1's random points to 3
        input_linked_list.head.random = input_linked_list.head.next_node.next_node

        # 2's random points to 1
        input_linked_list.head.next_node.random = input_linked_list.head

        # 3's random points to 5
        input_linked_list.head.next_node.next_node.random = input_linked_list.head.next_node.next_node.next_node.next_node

        # 4's random points to 5
        input_linked_list.head.next_node.next_node.next_node.random = input_linked_list.head.next_node.next_node.next_node.next_node

        # 5's random points to 2
        input_linked_list.head.next_node.next_node.next_node.next_node.random = input_linked_list.head.next_node

        copy_list_with_random_pointer_problem = CopyListWithRandomPointer(input_linked_list)

        # When
        output_list = copy_list_with_random_pointer_problem.solve()

        # Then
        self.assertEqual(output_list, [1, 2, 3, 4, 5])
