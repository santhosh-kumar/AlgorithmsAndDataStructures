"""
Unit Test for binary_indexed_tree
"""
from unittest import TestCase

from common.btree import BTree


class TestBTree(TestCase):
    """
    Unit test for BTree
    """

    def test_btree(self):
        """Test for construct

        Args:
            self: TestBinaryIndexedTree

        Returns:
            None

        Raises:
            None
        """
        # Given
        btree = BTree(10)

        # Then
        for i in range(10):
            btree.insert(i)

        self.assertEqual(str(btree), "Leaf BTreeNode with 10 keys\n	K:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n	C:[]\n")

    def test_search(self):
        """Test for search

        Args:
            self: TestBinaryIndexedTree

        Returns:
            None

        Raises:
            None
        """
        # Given
        btree = BTree(10)

        # Then
        for i in range(1000):
            btree.insert(i)

        node, index = btree.search(367)
        self.assertEqual(index, 7)
        self.assertEqual(node.keys, [i for i in range(360, 369)])
