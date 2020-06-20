"""
Check whether a binary tree is a full binary tree or not

A full binary tree is defined as a binary tree in which all nodes have either zero or two child nodes.
Conversely, there is no node in a full binary tree, which has one child node.

For example, given the below binary tree is full:

         1
        / \
       2   4
      / \
    2    3
"""

from common.problem import Problem


class CheckBinaryTreeIsFull(Problem):
    """
    Check Binary Tree Is Full
    """
    PROBLEM_NAME = "CheckBinaryTreeIsFull"

    def __init__(self, root_node):
        """CheckBinaryTreeIsFull

        Args:
            root_node: node of the tree

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.root_node = root_node

    def solve(self):
        """Solve the problem
        Note: O(n) (runtime) solution recursively checks the nodes for 0 or two children then it's full otherwise it's not.

        Args:

        Returns:
            boolean

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        return self.is_full_tree(self.root_node)

    @staticmethod
    def is_full_tree(root):
        """Solve the problem

        Args:
            root: node

        Returns:
            boolean

        Raises:
            None
        """
        # not a node, hence it's a valid tree
        if root is None:
            return True

        # no children, hence it's a valid tree
        if root.left is None and root.right is None:
            return True

        # if there are children, check the subtree recursively
        if root.left is not None and root.right is not None:
            return CheckBinaryTreeIsFull.is_full_tree(root.left) and CheckBinaryTreeIsFull.is_full_tree(root.right)

        # if we are here, it's not a full tree
        return False
