"""
This module defines a binary tree data structure.
"""
from collections import deque


class BinaryTreeNode:
    """
    An element (node) in a binary tree.
    """

    def __init__(self, data):
        """Init

        Args:
            data: Value of the node

        Returns:
            None

        Raises:
            None
        """
        super().__init__()
        self.data = data
        self.left = None
        self.right = None

    @staticmethod
    def in_order(node, elements_list):
        """Traverse the tree in order (similar to DFS) with O(n) complexity.

        Args:
            node: currently visited node
            elements_list: List to append values

        Returns:
            elements_list - in_order result

        Raises:
            None
        """
        if node is not None:
            BinaryTreeNode.in_order(node.left, elements_list)
            elements_list.append(node.data)
            BinaryTreeNode.in_order(node.right, elements_list)

    @staticmethod
    def pre_order(node, elements_list):
        """Traverse the tree in pre-order (similar to DFS) with O(n) complexity

        Args:
            node: currently visited node
            elements_list: List to append values

        Returns:
            elements_list - pre_order result

        Raises:
            None
        """
        if node is not None:
            elements_list.append(node.data)
            BinaryTreeNode.pre_order(node.left, elements_list)
            BinaryTreeNode.pre_order(node.right, elements_list)

    @staticmethod
    def post_order(node, elements_list):
        """Traverse the tree in pre-order (similar to DFS) with O(n) complexity

        Args:
            node: currently visited node
            elements_list: List to append values

        Returns:
            elements_list - post_order result

        Raises:
            None
        """
        if node is not None:
            BinaryTreeNode.post_order(node.left, elements_list)
            BinaryTreeNode.post_order(node.right, elements_list)
            elements_list.append(node.data)

    @staticmethod
    def level_order(root, elements_list):
        """Traverse the tree in level-order (similar to BFS) with O(n) complexity

        Args:
            root: root node
            elements_list: List to append values

        Returns:
            elements_list - post_order result

        Raises:
            None
        """
        if root is None:
            return

        nodes_queue = deque()
        nodes_queue.append(root)

        while len(nodes_queue) > 0:
            node = nodes_queue.popleft()

            elements_list.append(node.data)

            if node.left is not None:
                elements_list.append(node.left)

            if node.right is not None:
                elements_list.append(node.right)
