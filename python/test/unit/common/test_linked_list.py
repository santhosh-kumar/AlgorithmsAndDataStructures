"""
Unit Test for binary_tree
"""
from unittest import TestCase

from common.linked_list import LinkedList
from common.linked_list import Node


class TestLinkedList(TestCase):
    """
    Unit test for LinkedList
    """

    def test_construct(self):
        """Test for construct

        Args:
            self: TestLinkedList

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

        # Then
        self.assertEqual(input_linked_list.output_list(), [1, 2, 3, 4, 5])
