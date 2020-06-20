"""
Check Binary Tree is a subtree of another Binary Tree

Given two binary trees, check if the first tree is subtree of the second one.
A subtree of a tree T is a tree S consisting of a node in T and all of its descendants in T.
The subtree corresponding to the root node is the entire tree;
the subtree corresponding to any other node is called a proper subtree.

For example, in the following case, tree S is a subtree of tree T.

        Tree 2
          10
        /    \
      4       6
       \
        30


        Tree 1
              26
            /   \
          10     3
        /    \     \
      4       6      3
       \
        30
"""

from common.problem import Problem


class CheckBinaryTreeIsSubtree(Problem):
    """
    Check Binary Tree Is Subtree
    """
    PROBLEM_NAME = "CheckBinaryTreeIsSubtree"

    def __init__(self, root_node1, root_node2):
        """CheckBinaryTreeIsSubtree

        Args:
            root_node1: node of the 1st tree
            root_node2: node of the 2nd tree

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.root_node1 = root_node1
        self.root_node2 = root_node2

    def solve(self):
        """Solve the problem
        Note: O(nm) (runtime) solution recursively compares two trees.

        Args:

        Returns:
            boolean

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        if self.root_node2 is None:
            return True

        if self.root_node2 is None:
            return True

        return self.are_identical(self.root_node1, self.root_node2) or \
               self.are_identical(self.root_node1.left, self.root_node2) or \
               self.are_identical(self.root_node1.right, self.root_node2)

    @staticmethod
    def are_identical(root1, root2):
        """Check if the trees are identical recursively

        Args:
            root1: First root node
            root2: Second root node

        Returns:
            boolean

        Raises:
            None
        """
        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        return (root1.data == root2.data) and \
               CheckBinaryTreeIsSubtree.are_identical(root1.left, root2.left) and \
               CheckBinaryTreeIsSubtree.are_identical(root1.right, root2.right)
