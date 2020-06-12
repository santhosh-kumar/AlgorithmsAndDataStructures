"""
Binary Tree Upside Down

Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left
node that shares the same parent node) or empty, flip it upside down and turn it into a tree
where the original right nodes turned into left leaf nodes. Return the new root.

For example:

Given a binary tree {1,2,3,4,5},

    1
   / \
  2   3
 / \
4   5
return the root of the binary tree [4,5,2,#,#,3,1].

   4
  / \
 5   2
    / \
   3   1
"""
from common.problem import Problem


class BinaryTreeUpsideDown(Problem):
    """
    Binary Tree Upside Down
    """
    PROBLEM_NAME = "BinaryTreeUpsideDown"

    def __init__(self, root_node):
        """Binary Tree Upside Down

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

        Note: O(n) (runtime) and O(1) space complexity.

        Args:

        Returns:
            BinaryTreeNode

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        node = self.root_node
        parent = None
        parent_right = None

        while node is not None:
            left = node.left
            node.left = parent_right
            parent_right = node.right
            node.right = parent
            parent = node
            node = left

        return parent
