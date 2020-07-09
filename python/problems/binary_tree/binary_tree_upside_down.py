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

            Reference: https://medium.com/@jimdaosui/binary-tree-upside-down-77af203c79af
            1) If the current root has left child, make the left child right point to the current root.
            2) If the current root has left child, make the left child left point to the current root.
            3) Repeat the operations above until the current root does not have left child.

        Args:

        Returns:
            BinaryTreeNode

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        previous_node = None
        last_right_node = None
        current_node = self.root_node

        # idea is similar to reversing a linked-list
        while current_node is not None:
            next_node = current_node.left
            current_node.left = last_right_node

            last_right_node = current_node.right
            current_node.right = previous_node

            previous_node = current_node
            current_node = next_node

        return previous_node
