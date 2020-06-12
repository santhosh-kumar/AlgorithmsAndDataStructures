"""
Validate Binary Search Tree (Brute Force)

Given a binary tree, determine if it is a valid Binary Search Tree (BST).

A BST is based on binary tree, but with the following additional properties:
- The left subtree of a node contains only nodes with keys less than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s key.
- Both the left and right subtrees must also be binary search trees

"""
from common.problem import Problem


class ValidateBinarySearchTreeBruteForce(Problem):
    """
    Validate Binary Search Tree (Brute Force)
    """
    PROBLEM_NAME = "ValidateBinarySearchTreeBruteForce"

    def __init__(self, root_node):
        """Validate Binary Search Tree (Brute Force)

        Args:
            root_node: node of the tree to be validated

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.root_node = root_node

    def solve(self):
        """Solve the problem

        Note: O(n^2) (runtime) and O(n) (stack space due to recursive calls) solution works by iterating from the current node and traversing left subtree to check
        if the node values are lesser than the current node.
        Then, traverse the right subtree to check if the node values are greater than the current node's value.

        Args:

        Returns:
            boolean

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        return self.is_valid_binary_search_tree(self.root_node)

    @staticmethod
    def is_valid_binary_search_tree(root):
        """Check if the given is a valid binary search tree

        Args:
            root: node of the tree

        Returns:
            boolean

        Raises:
            None
        """
        if root is None:
            return True

        return ValidateBinarySearchTreeBruteForce.is_subtree_lesser_than(root.left,
                                                                         root.data) and ValidateBinarySearchTreeBruteForce.is_subtree_greater_than(
            root.right, root.data) and ValidateBinarySearchTreeBruteForce.is_valid_binary_search_tree(
            root.left) and ValidateBinarySearchTreeBruteForce.is_valid_binary_search_tree(root.right)

    @staticmethod
    def is_subtree_lesser_than(node, value):
        """Check if the subtree is lesser than given node's and the parent value
        Args:
            node: Given node
            value: parent node value

        Returns:
            boolean

        Raises:
            None
        """
        if node is None:
            return True

        return node.data < value and ValidateBinarySearchTreeBruteForce.is_subtree_lesser_than(node.left,
                                                                                               value) and ValidateBinarySearchTreeBruteForce.is_subtree_lesser_than(
            node.right, value)

    @staticmethod
    def is_subtree_greater_than(node, value):
        """Check if the subtree is greater than given node's and the parent value
        Args:
            node: Given node
            value: parent node value

        Returns:
            boolean

        Raises:
            None
        """
        if node is None:
            return True

        return node.data > value and ValidateBinarySearchTreeBruteForce.is_subtree_greater_than(node.left,
                                                                                                value) and ValidateBinarySearchTreeBruteForce.is_subtree_greater_than(
            node.right, value)
