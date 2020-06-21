"""
Right View of Binary Tree

Given a Binary Tree, print Right view of it.
Right view of a Binary Tree is set of nodes visible when tree is visited from Right side.

Right view of following tree is 1 3 7 8

          1
       /     \
     2        3
   /   \     /  \
  4     5   6    7
                  \
                   8
"""
from common.problem import Problem


class RightViewOfBinaryTree(Problem):
    """
    Right View of Binary Tree
    """
    PROBLEM_NAME = "RightViewOfBinaryTree"

    def __init__(self, root_node):
        """Right View of Binary Tree

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
        Note: O(n) (runtime) solution iterates through the right side first and record the maximum level it went.
        Then, it iterates through the left side, it records the left side only if it's in a higher level.

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        max_level = [0]
        right_view_list = []
        self.right_view(self.root_node, 1, max_level, right_view_list)
        return right_view_list

    def right_view(self, root, level, max_level, right_view_list):
        """Right View

        Args:
            root:
            level:
            max_level:
            right_view_list:

        Returns:
            list

        Raises:
            None
        """
        # Base Case
        if root is None:
            return

        # If this is the last node of its level
        if max_level[0] < level:
            right_view_list.append(root.data)
            max_level[0] = level

        # Recur for right subtree first, then left subtree
        self.right_view(root.right, level + 1, max_level, right_view_list)
        self.right_view(root.left, level + 1, max_level, right_view_list)
