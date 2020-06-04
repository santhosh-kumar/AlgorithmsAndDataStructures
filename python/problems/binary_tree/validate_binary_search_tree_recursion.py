"""
Validate Binary Search Tree (Recursion)

Given a binary tree, determine if it is a valid Binary Search Tree (BST).

A BST is based on binary tree, but with the following additional properties:
- The left subtree of a node contains only nodes with keys less than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s key.
- Both the left and right subtrees must also be binary search trees

"""
from common.problem import Problem


class ValidateBinarySearchTreeRecursion(Problem):
    """
    Validate Binary Search Tree (Brute Force)
    """
    PROBLEM_NAME = "ValidateBinarySearchTreeRecursion"

    def __init__(self, root_node):
        """Validate Binary Search Tree (Top Down Recursion)

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
            Note: For O(n) (runtime) and O(n) (stack space due to recursion) solution, we can avoid examining all nodes of both subtrees in
            each pass by passing down the low and high limits from the parent to its children.

        Args:

        Returns:
            boolean

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        return self.is_valid_binary_search_tree(self.root_node, None, None)

    @staticmethod
    def is_valid_binary_search_tree(root, low, high):
        """Check if the given is a valid binary search tree
        Args:
            root: node of the tree
            low: lowest value
            high: highest value

        Returns:
            boolean

        Raises:
            None
        """
        if root is None:
            return True

        return (low is None or root.data > low) and (
                high is None or root.data < high) and ValidateBinarySearchTreeRecursion.is_valid_binary_search_tree(
            root.left, low, root.data) and ValidateBinarySearchTreeRecursion.is_valid_binary_search_tree(root.right,
                                                                                                         root.data,
                                                                                                         high)
