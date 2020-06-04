"""
Validate Binary Search Tree (In Order Tree Traversal Based solution)

Given a binary tree, determine if it is a valid Binary Search Tree (BST).

A BST is based on binary tree, but with the following additional properties:
- The left subtree of a node contains only nodes with keys less than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s key.
- Both the left and right subtrees must also be binary search trees

"""
from common.problem import Problem


class ValidateBinarySearchTreeInOrderTraversal(Problem):
    """
    Validate Binary Search Tree (In Order Traversal)
    """
    PROBLEM_NAME = "ValidateBinarySearchTreeInOrderTraversal"

    def __init__(self, root_node):
        """Validate Binary Search Tree (In Order Traversal)

        Args:
            root_node: node of the tree to be validated

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.root_node = root_node
        self.previous_value = None

    def solve(self):
        """Solve the problem
            Note: O(n) (runtime) and O(n) (stack space) solution works by using the in order traversal,
            and verifying that previous node is lesser than the current node.

        Args:

        Returns:
            boolean

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        return self.is_valid_binary_search_tree(self.root_node)

    def is_valid_binary_search_tree(self, root):
        """Check if the given is a valid binary search tree
        Args:
            root: node of the tree

        Returns:
            boolean

        Raises:
            None
        """
        return self.is_monotonically_increasing(root)

    def is_monotonically_increasing(self, node):
        """Check if the tree node is monotonically increasing
        Args:
            node: node of the tree

        Returns:
            boolean

        Raises:
            None
        """
        if node is None:
            return True

        # Visit Left Node
        if self.is_monotonically_increasing(node.left):

            # Root node should be greater than the left node
            if self.previous_value is not None and node.data <= self.previous_value:
                return False

            # Record the node value
            self.previous_value = node.data

            # Check the right node
            return self.is_monotonically_increasing(node.right)

        # If we are here, we
        return False
