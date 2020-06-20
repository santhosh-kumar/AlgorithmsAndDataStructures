"""
Unit Test for unionfind
"""
from unittest import TestCase

from common.binary_indexed_tree import BinaryIndexedTree


class TestBinaryIndexedTree(TestCase):
    """
    Unit test for BinaryIndexedTree
    """

    def test_binary_indexed_tree(self):
        """Test for construct & get_sum

        Args:
            self: TestBinaryIndexedTree

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        binary_indexed_tree = BinaryIndexedTree(input_array)

        # Then
        for i in range(len(input_array)):
            total_sum = (i * (i + 1) / 2)
            self.assertEqual(binary_indexed_tree.get_sum(i), total_sum)
