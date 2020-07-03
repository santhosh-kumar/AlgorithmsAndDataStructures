"""
Unit Test for binary_tree
"""
from unittest import TestCase

from common.binary_tree import BinaryTreeNode


class TestBinaryTree(TestCase):
    """
    Unit test for BinaryTree
    """

    def test_construct(self):
        """Test for construct

        Args:
            self: TestBinaryTree

        Returns:
            None

        Raises:
            None
        """
        # Given
        root = BinaryTreeNode(3)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(5)
        root.right.left = BinaryTreeNode(4)
        root.right.right = BinaryTreeNode(7)
        root.right.right.right = BinaryTreeNode(8)
        root.right.right.left = BinaryTreeNode(6)

        # Then
        self.assertEqual(root.data, 3)
        self.assertEqual(root.left.data, 2)
        self.assertEqual(root.right.data, 5)
        self.assertEqual(root.right.left.data, 4)
        self.assertEqual(root.right.right.data, 7)
        self.assertEqual(root.right.right.right.data, 8)
        self.assertEqual(root.right.right.left.data, 6)

    def test_in_order_traversal(self):
        """Test for in_order

        Args:
            self: TestBinaryTree

        Returns:
            None

        Raises:
            None
        """
        # Given
        root = BinaryTreeNode(3)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(5)
        root.right.left = BinaryTreeNode(4)
        root.right.right = BinaryTreeNode(7)
        root.right.right.right = BinaryTreeNode(8)
        root.right.right.left = BinaryTreeNode(6)

        # When
        result = []
        BinaryTreeNode.in_order(root, result)

        # Then
        self.assertEqual(result, [2, 3, 4, 5, 6, 7, 8])

    def test_pre_order_traversal(self):
        """Test for pre_order

        Args:
            self: TestBinaryTree

        Returns:
            None

        Raises:
            None
        """
        # Given
        root = BinaryTreeNode(3)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(5)
        root.right.left = BinaryTreeNode(4)
        root.right.right = BinaryTreeNode(7)
        root.right.right.right = BinaryTreeNode(8)
        root.right.right.left = BinaryTreeNode(6)

        # When
        result = []
        BinaryTreeNode.pre_order(root, result)

        # Then
        self.assertEqual(result, [3, 2, 5, 4, 7, 6, 8])

    def test_post_order_traversal(self):
        """Test for post_order

        Args:
            self: TestBinaryTree

        Returns:
            None

        Raises:
            None
        """
        # Given
        root = BinaryTreeNode(3)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(5)
        root.right.left = BinaryTreeNode(4)
        root.right.right = BinaryTreeNode(7)
        root.right.right.right = BinaryTreeNode(8)
        root.right.right.left = BinaryTreeNode(6)

        # When
        result = []
        BinaryTreeNode.post_order(root, result)

        # Then
        self.assertEqual(result, [2, 4, 6, 8, 7, 5, 3])
